"""agent_loop.py — Importable streaming conversation loop helper.

Usage in any notebook cell:
    from agent_loop import run_conversation, print_steps

    # Stream only
    await run_conversation('I am a Python tutor. How can I help you?', tutor)

    # Stream + show ReAct steps after each turn
    await run_conversation('I am a Python tutor. How can I help you?', tutor, show_steps=True)

    # Show steps for a run you already have
    print_steps(result.new_items)

Environment detection
---------------------
In Jupyter notebooks, responses stream as live-updating rendered Markdown.
In a command-line IPython session, the in-place update protocol is not
supported, so the helper falls back to plain print() streaming and prints
step traces as plain text.
"""

import json as _json
from agents import Agent, Runner
from IPython.display import HTML, Markdown, display
from openai.types.responses import ResponseTextDeltaEvent


def _is_jupyter() -> bool:
    """Return True when running inside a Jupyter kernel (notebook or JupyterLab)."""
    try:
        shell = get_ipython().__class__.__name__   # type: ignore[name-defined]
        return shell == 'ZMQInteractiveShell'      # Jupyter kernel
    except NameError:
        return False                               # plain Python script


def print_steps(new_items) -> None:
    """Render the ReAct step trace from a completed run.

    Displays as rendered Markdown in Jupyter; falls back to plain text
    in a command-line IPython session.

    Args:
        new_items: result.new_items from a RunResultStreaming object.
    """
    lines = ['---', '**Steps**', '']
    for i, item in enumerate(new_items, 1):
        raw = getattr(item, 'raw_item', None)
        item_type = getattr(raw, 'type', type(item).__name__) if raw else type(item).__name__
        line = f'**Step {i}** — `{item_type}`'
        if raw and hasattr(raw, 'name'):
            line += f'  \nTool: `{raw.name}`'
        if raw and hasattr(raw, 'arguments'):
            try:
                args = _json.loads(raw.arguments)
                line += f'  \nArgs: `{args}`'
            except Exception:
                pass
        lines.append(line)
        lines.append('')

    md = '\n'.join(lines)

    if _is_jupyter():
        display(Markdown(md))
    else:
        # Plain-text fallback: strip markdown symbols
        print('--- Steps ---')
        for i, item in enumerate(new_items, 1):
            raw = getattr(item, 'raw_item', None)
            item_type = getattr(raw, 'type', type(item).__name__) if raw else type(item).__name__
            print(f'  Step {i} [{item_type}]')
            if raw and hasattr(raw, 'name'):
                print(f'    Tool: {raw.name}')
            if raw and hasattr(raw, 'arguments'):
                try:
                    print(f'    Args: {_json.loads(raw.arguments)}')
                except Exception:
                    pass
        print()


async def run_conversation(intro: str, agent: Agent, show_steps: bool = False) -> None:
    """Run an interactive streaming conversation loop with an agent.

    In Jupyter, responses render as live-updating Markdown.
    In a command-line IPython session, responses stream via plain print().

    Args:
        intro: Message printed at the start of the conversation.
        agent: The Agent to converse with.
        show_steps: If True, renders the ReAct step trace after each turn.
    """
    print(intro)
    previous_response_id = None
    turn_count = 1

    while (prompt := input(f'\nInput [{turn_count}]: ')) != 'exit':
        result = Runner.run_streamed(
            agent,
            prompt,
            previous_response_id=previous_response_id,
            auto_previous_response_id=True
        )

        if _is_jupyter():
            display(HTML('<div style="height: 1em;"></div>'))  # blank line after input
            markdown_text = ''
            handle = display(Markdown(markdown_text), display_id=True)

            async for event in result.stream_events():
                if (event.type == 'raw_response_event' and
                        isinstance(event.data, ResponseTextDeltaEvent)):
                    markdown_text += event.data.delta
                    handle.update(Markdown(markdown_text))
        else:
            print()
            async for event in result.stream_events():
                if (event.type == 'raw_response_event' and
                        isinstance(event.data, ResponseTextDeltaEvent)):
                    print(event.data.delta, end='', flush=True)
            print()

        if show_steps:
            print_steps(result.new_items)

        turn_count += 1

        if _is_jupyter():
            display(HTML('<hr>'))
        else:
            print('-' * 60)

        previous_response_id = result.last_response_id

    print('User terminated app.')
