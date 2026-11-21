"""Command-line realtime voice weather agent.

Run from the repository root:
    python source/realtime_voice_weather_agent.py

The app greets you, asks how it can help, then listens continuously. Server-side
voice activity detection recognizes when you stop speaking. The script sends
microphone audio to an OpenAI Realtime model over WebSocket, prints live
response transcript deltas, and plays the model's streamed voice response.
Press Ctrl+C to quit.
"""

from __future__ import annotations

import argparse
import asyncio
import locale
import re
import threading

from agents.mcp import MCPServerStreamableHttp
from agents.realtime import (
    RealtimeAgent,
    RealtimeAudio,
    RealtimeAudioEnd,
    RealtimeError,
    RealtimeModelInputAudioTranscriptionCompletedEvent,
    RealtimeModelTranscriptDeltaEvent,
    RealtimeModelTurnStartedEvent,
    RealtimeRawModelEvent,
    RealtimeRunner,
    RealtimeToolEnd,
    RealtimeToolStart,
)


WEATHER_MCP_URL = 'https://weather.chukai.io/mcp'

# The Realtime API can stream raw PCM16 audio. PCM16 means 16-bit signed
# integer samples with no WAV/MP3 container. That is convenient for live audio
# because each chunk can be sent or played immediately without file encoding.
SAMPLE_RATE = 24_000

# Keep microphone chunks small so the model receives audio with low latency.
# 0.1 seconds at 24 kHz mono PCM16 is 2400 samples / 4800 bytes.
MICROPHONE_BLOCK_SECONDS = 0.1

WEATHER_INSTRUCTIONS = """
You are a concise voice-first weather assistant with worldwide coverage.

The weather MCP server provides geocoding and weather tools. When the user
gives a city or place name, use geocoding first to get coordinates, then use
the weather tools.

Respond conversationally in two or three short paragraphs. Include the
location, current conditions or forecast, temperature, wind, and any active
alerts when relevant. Avoid tables because this response will be read aloud.

Use the user's locale to choose default units and language:
- United States locales: imperial units by default, such as Fahrenheit and mph.
- Most other locales: metric units by default, such as Celsius and km/h.
- If the user asks for different units, use the requested units.
- Speak in the user's locale language when it is clear and supported, but follow
  any language the user explicitly requests.

If the transcript is only a tiny accidental sound, cough, swallow, or unclear
fragment, do not answer it as a real request. Briefly wait for a clearer weather
question.
"""

EXIT_PHRASES = {
    'exit',
    'quit',
    'goodbye',
    'good bye',
    'stop listening',
    'terminate',
}

NOISE_TRANSCRIPTS = {
    '',
    '.',
    '..',
    '...',
    'uh',
    'um',
    'ah',
    'hmm',
    'mm',
    'mhm',
}

MIN_REQUEST_WORDS = 3


def import_sounddevice():
    """Import sounddevice with a clear setup message for existing environments."""
    try:
        import sounddevice as sd
    except ModuleNotFoundError as error:
        raise SystemExit(
            'The sounddevice package is required for microphone/audio playback.\n'
            'Install it in this environment with:\n\n'
            '    python -m pip install sounddevice\n\n'
            'Then rerun this script.'
        ) from error
    return sd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Talk with a realtime OpenAI weather agent from the command line.'
    )
    parser.add_argument(
        '--voice', default='marin',
        help='Realtime voice name'
    )
    parser.add_argument(
        '--model', default='gpt-realtime',
        help='Realtime model name'
    )
    parser.add_argument(
        '--locale', default=get_default_locale(),
        help='locale hint for units and spoken language, such as en_US or fr_FR'
    )
    return parser.parse_args()


def get_default_locale() -> str:
    """Return the system locale, falling back to en_US."""
    system_locale = locale.getlocale()[0]
    return system_locale or 'en_US'


def locale_guidance(locale_name: str) -> str:
    """Create model-visible instructions for locale-sensitive responses."""
    language = locale_name.split('_', maxsplit=1)[0].lower()
    country = locale_name.split('_', maxsplit=1)[1].upper() if '_' in locale_name else ''
    units = 'imperial' if country == 'US' else 'metric'
    return (
        f'The user locale is {locale_name}. Use {units} units by default. '
        f'Use language code {language} as the default spoken language unless '
        'the user speaks or requests another language.'
    )


def normalize_transcript(text: str) -> str:
    """Normalize transcript text for command/noise detection."""
    text = text.strip().lower()
    text = re.sub(r'[^\w\s]', '', text)
    return re.sub(r'\s+', ' ', text)


def is_exit_command(text: str) -> bool:
    """Return True when the user asks to quit."""
    normalized = normalize_transcript(text)
    return normalized in EXIT_PHRASES or normalized.startswith('exit ')


def looks_like_noise(text: str) -> bool:
    """Return True for tiny accidental transcript fragments."""
    normalized = normalize_transcript(text)
    if normalized in NOISE_TRANSCRIPTS:
        return True
    words = normalized.split()
    return len(words) < MIN_REQUEST_WORDS


def response_request(transcript: str) -> str:
    """Wrap an accepted transcript with response style instructions."""
    # The realtime session first transcribes speech. We intentionally do not let
    # every audio turn automatically produce an answer, because coughs, chair
    # sounds, and other background noise can sometimes become tiny transcripts.
    # Instead, once the transcript passes local filtering, we send this text
    # message back into the same realtime conversation and ask the agent to
    # respond. This gives us a clean place to add UX instructions.
    return (
        f'The user said: "{transcript}"\n\n'
        'If this is a weather request, first say a very short, natural, varied '
        'acknowledgement before using tools. Do not repeat the full location or '
        'parrot the user. Good examples: "Sure, let me check that.", "One moment.", '
        '"Hang on.", "Let me take a look.", or "I’ll check." Vary this phrasing '
        'across turns so the conversation feels natural. Then use the weather '
        'tools and answer. If it is not a weather request, briefly explain that '
        'this demo is a weather voice agent and ask for a weather question.'
    )


async def stream_microphone(
    session,
    stop_event: asyncio.Event,
    pause_microphone: threading.Event
) -> None:
    """Continuously stream microphone audio to the realtime session."""
    sd = import_sounddevice()
    loop = asyncio.get_running_loop()
    audio_queue: asyncio.Queue[bytes | None] = asyncio.Queue()

    def callback(indata, _frames, _time, status):
        # sounddevice calls this function from an audio callback thread, not
        # from the asyncio event loop. We cannot safely await or call async
        # APIs here. Instead, copy the bytes and hand them to the asyncio loop
        # with call_soon_threadsafe().
        if status:
            print(f'\n[microphone] {status}')
        if not pause_microphone.is_set():
            loop.call_soon_threadsafe(audio_queue.put_nowait, bytes(indata))

    async def sender() -> None:
        # This coroutine is the bridge from the microphone callback thread to
        # the Realtime API WebSocket. Each queue item is a raw PCM16 chunk.
        while True:
            chunk = await audio_queue.get()
            if chunk is None or stop_event.is_set():
                break
            if pause_microphone.is_set():
                # Drop buffered input while the assistant is speaking. Without
                # this gate, the microphone may hear the speakers and the model
                # may interrupt itself or answer its own audio.
                continue
            await session.send_audio(chunk)

    print('Listening. Speak naturally; pause when you finish a turn.')
    sender_task = asyncio.create_task(sender())

    try:
        with sd.RawInputStream(
            # RawInputStream gives us PCM bytes directly. A normal InputStream
            # would give NumPy arrays; either works, but raw bytes map directly
            # to the Realtime API's pcm16 input format.
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16',
            blocksize=int(SAMPLE_RATE * MICROPHONE_BLOCK_SECONDS),
            callback=callback
        ):
            await stop_event.wait()
    finally:
        stop_event.set()
        await audio_queue.put(None)
        await sender_task


async def send_greeting(session) -> None:
    """Ask the realtime agent to greet the user at startup."""
    # This is a text message sent into the realtime session. Because the session
    # output modality is audio, the model responds with both streamed audio and
    # transcript deltas, just as it does after user speech.
    await session.send_message(
        'Greet me warmly in one sentence and ask how you can help with the weather.'
    )


async def run_realtime_weather_agent(args: argparse.Namespace) -> None:
    """Run the realtime microphone -> agent -> speaker loop."""
    async with MCPServerStreamableHttp(
        params={'url': WEATHER_MCP_URL},
        cache_tools_list=True
    ) as weather_server:
        agent = RealtimeAgent(
            name='RealtimeVoiceWeatherAssistant',
            instructions=f'{WEATHER_INSTRUCTIONS}\n\n{locale_guidance(args.locale)}',
            mcp_servers=[weather_server]
        )

        runner = RealtimeRunner(agent)
        model_config = {
            'initial_model_settings': {
                # gpt-realtime is the current default realtime model family.
                # The user can override this with --model for experiments.
                'model_name': args.model,

                # Audio-only mode means the model's user-facing responses are
                # spoken. We still receive transcript events for display.
                'modalities': ['audio'],
                'voice': args.voice,

                # These must match the bytes we record/play with sounddevice.
                'input_audio_format': 'pcm16',
                'output_audio_format': 'pcm16',

                # Request server-side transcription of user audio. The app uses
                # these transcripts for display, spoken "exit" detection, and
                # local filtering of likely background sounds.
                'input_audio_transcription': {'model': 'gpt-4o-transcribe'},
                'turn_detection': {
                    # server_vad means the Realtime service detects speech
                    # boundaries. The app streams audio continuously; the server
                    # decides when the user appears to have stopped speaking.
                    'type': 'server_vad',

                    # We set this to False so every detected sound does not
                    # automatically produce a model response. Instead, this app
                    # waits for the transcript, filters it locally, then sends a
                    # text message asking the agent to respond only when the
                    # transcript looks like an intentional request.
                    'create_response': False,

                    # Tune VAD to be less eager in a classroom/office. If the
                    # app misses quiet speech, lower threshold or silence time.
                    'threshold': 0.7,
                    'silence_duration_ms': 900,
                    'prefix_padding_ms': 300,

                    # Keep the assistant from being interrupted by incidental
                    # microphone pickup while it is speaking.
                    'interrupt_response': False,
                },
                'tracing': {'workflow_name': 'realtime-voice-weather-agent'},
            }
        }

        async with await runner.run(model_config=model_config) as session:
            print('Realtime voice weather agent ready.')
            print('Press Ctrl+C to quit.')

            stop_microphone = asyncio.Event()
            stop_session = asyncio.Event()
            pause_microphone = threading.Event()
            pause_microphone.set()  # Do not let the mic hear the startup greeting.
            microphone_task = asyncio.create_task(
                stream_microphone(session, stop_microphone, pause_microphone)
            )
            response_started = False
            sd = import_sounddevice()

            await send_greeting(session)

            try:
                with sd.RawOutputStream(
                    # RawOutputStream accepts the PCM16 bytes emitted by the
                    # Realtime model. No MP3/WAV file is created.
                    samplerate=SAMPLE_RATE,
                    channels=1,
                    dtype='int16'
                ) as output_stream:
                    async for event in session:
                        # The Agents SDK normalizes many events, but transcript
                        # deltas and input transcription completions arrive as
                        # raw model events wrapped in RealtimeRawModelEvent.
                        if isinstance(event, RealtimeRawModelEvent):
                            data = event.data
                            if isinstance(data, RealtimeModelInputAudioTranscriptionCompletedEvent):
                                transcript = data.transcript.strip()
                                print(f'\nYou said: {transcript}')
                                if is_exit_command(transcript):
                                    # Spoken app-control command. We interrupt
                                    # any pending response and leave the loop.
                                    print('Exit requested. Stopping...')
                                    stop_session.set()
                                    await session.interrupt()
                                    break
                                if looks_like_noise(transcript):
                                    # This catches common cases where VAD
                                    # correctly detects sound but the transcript
                                    # is not a real request, such as "uh".
                                    print('[ignored likely background sound]')
                                    await session.interrupt()
                                else:
                                    # A real transcript becomes an explicit text
                                    # message in the same realtime session. This
                                    # is what triggers the assistant response.
                                    pause_microphone.set()
                                    await session.send_message(response_request(transcript))
                            elif isinstance(data, RealtimeModelTurnStartedEvent):
                                # The assistant is starting to respond. Pause
                                # the mic so speaker audio is not sent back in.
                                pause_microphone.set()
                                response_started = False
                            elif isinstance(data, RealtimeModelTranscriptDeltaEvent):
                                # These are the assistant's streamed words. They
                                # are useful for demos and accessibility because
                                # attendees can see the same response they hear.
                                if not response_started:
                                    print('\nAssistant: ', end='', flush=True)
                                    response_started = True
                                print(data.delta, end='', flush=True)

                        elif isinstance(event, RealtimeToolStart):
                            # Tool events make it clear when the agent is using
                            # the hosted MCP weather server instead of answering
                            # from model knowledge alone.
                            print(f'\n[tool start] {event.tool.name}: {event.arguments}')

                        elif isinstance(event, RealtimeToolEnd):
                            print(f'\n[tool end] {event.tool.name}')

                        elif isinstance(event, RealtimeAudio):
                            # The model emits many small PCM16 audio chunks.
                            # Writing in a worker thread avoids blocking the
                            # asyncio event loop while audio hardware plays.
                            pause_microphone.set()
                            await asyncio.to_thread(output_stream.write, event.audio.data)

                        elif isinstance(event, RealtimeAudioEnd):
                            # Once the assistant is done speaking, resume
                            # forwarding microphone chunks to the model.
                            print()
                            pause_microphone.clear()

                        elif isinstance(event, RealtimeError):
                            print(f'\nRealtime error: {event.error}')
                            if stop_session.is_set():
                                break
            finally:
                stop_microphone.set()
                await microphone_task

    print('Realtime voice weather agent stopped.')


if __name__ == '__main__':
    asyncio.run(run_realtime_weather_agent(parse_args()))
