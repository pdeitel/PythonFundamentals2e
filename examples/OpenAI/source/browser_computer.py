"""LocalBrowserComputer — AsyncComputer implementation backed by Playwright.

Used by 02-05-07-computer-tool-accuweather.ipynb.
Import with:
    from source.browser_computer import LocalBrowserComputer

NOTE: The code in this file was created by a combination of OpenAI Codex
and Claude Code for demo purposes.
"""

import asyncio
import base64
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Literal

from playwright.async_api import Browser, Page, Playwright, async_playwright
from agents import AsyncComputer, Button

# `ComputerTool` does not know anything about Playwright. It talks to an
# object that implements the `AsyncComputer` interface. When the model chooses
# a computer action, the Agents SDK calls methods on this object such as
# `screenshot`, `click`, `type`, `scroll` and `keypress`.
#
# Playwright is just the implementation detail we use here. It gives us a
# controllable Chromium browser without moving the real OS mouse or typing into
# whatever app the presenter is using.

# ComputerTool key names are model-facing names, such as "ctrl" and "enter".
# Playwright expects browser-driver names, such as "Control" and "Enter".
# This map translates the common key names the model may request.
KEY_MAP = {
    '/':          'Slash',    # regular forward-slash; 'Divide' is the numpad key
    '\\':         'Backslash',
    'alt':        'Alt',
    'arrowdown':  'ArrowDown',
    'arrowleft':  'ArrowLeft',
    'arrowright': 'ArrowRight',
    'arrowup':    'ArrowUp',
    'backspace':  'Backspace',
    'cmd':        'Meta',
    'ctrl':       'Control',
    'delete':     'Delete',
    'end':        'End',
    'enter':      'Enter',
    'esc':        'Escape',
    'escape':     'Escape',
    'home':       'Home',
    'meta':       'Meta',
    'option':     'Alt',
    'pagedown':   'PageDown',
    'pageup':     'PageUp',
    'pgdn':       'PageDown',
    'pgup':       'PageUp',
    'return':     'Enter',
    'shift':      'Shift',
    'space':      ' ',
    'tab':        'Tab'
}


class LocalBrowserComputer(AsyncComputer):
    """Playwright-backed AsyncComputer implementation for browser interaction.

    Drives a local Chromium browser via Chrome DevTools Protocol (CDP).
    The OS mouse and keyboard are NOT used — the user can work in other
    apps freely while the agent operates the browser.

    Args:
        start_url:  URL to open when the browser launches.
        channel:    Playwright browser channel. Use 'chrome' for the system
                    installation of Google Chrome, or omit (None) to use
                    Playwright's bundled Chromium. 'chromium' is NOT a valid
                    channel name and will raise a Playwright error.
        headless:   True to run without a visible window (e.g. CI).
                    False (default) opens a visible window for demos.
    """

    def __init__(
        self,
        start_url: str       = 'https://www.accuweather.com/',
        channel:   str | None = None,   # None = bundled Playwright Chromium; 'chrome' = system Chrome
        headless:  bool       = False,
    ):
        # These values configure the browser session but do not launch it yet.
        # Launching is asynchronous, so it happens in `__aenter__` below.
        self.start_url = start_url
        self.channel   = channel
        self.headless  = headless

        # Set in __aenter__; None until the browser has launched.
        # Keeping these attributes separate makes cleanup explicit in
        # `__aexit__` and avoids hiding browser lifecycle work in properties.
        self.playwright_instance: Playwright | None = None
        self.browser_instance:   Browser    | None = None
        self.page_instance:      Page       | None = None

    @property
    def environment(self) -> str:
        # The Agents SDK sends this environment label to the model.
        # "browser" tells the model the computer surface is a web browser,
        # so browser-oriented actions like clicking links, typing in fields
        # and scrolling pages are appropriate.
        return 'browser'

    @property
    def dimensions(self) -> tuple[int, int]:
        # The SDK sends this size with screenshots so model coordinates match
        # the browser viewport. Larger sizes show more page content but also
        # produce larger screenshots for the model to process.
        return (1280, 900)

    @property
    def page(self) -> Page:
        # Most action methods need the Playwright Page object. If a notebook
        # calls one of those methods before entering the async context manager,
        # this assertion gives a clear setup error instead of a NoneType error.
        assert self.page_instance is not None, 'Browser not started'
        return self.page_instance

    async def __aenter__(self):
        """Launch Playwright, open the browser, and navigate to start_url."""
        width, height = self.dimensions

        # Start the Playwright driver process. This is separate from the browser
        # process; stopping it in `__aexit__` prevents background processes from
        # accumulating during repeated notebook runs.
        self.playwright_instance = await async_playwright().start()

        # Launch Chromium. `headless=False` is best for live demos because the
        # presenter can watch the browser move. In automated runs, set headless=True.
        self.browser_instance = await self.playwright_instance.chromium.launch(
            channel=self.channel,
            headless=self.headless,
            args=[f'--window-size={width},{height}'],
        )

        # Create one tab and force the viewport to match `dimensions`. The model
        # will later click coordinates that refer to screenshots of this tab.
        self.page_instance = await self.browser_instance.new_page()
        await self.page.set_viewport_size({'width': width, 'height': height})

        # Load the starting page before the agent gets control. `domcontentloaded`
        # keeps startup fast; the later `wait()` method gives dynamic pages time
        # to settle when needed.
        await self.page.goto(self.start_url, wait_until='domcontentloaded')
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """Close the browser and stop Playwright when the context exits."""
        # Always release browser resources, even if the agent run raises an
        # exception. This matters in notebooks because cells are often re-run.
        if self.browser_instance:
            await self.browser_instance.close()
        if self.playwright_instance:
            await self.playwright_instance.stop()

    # ------------------------------------------------------------------ #
    # AsyncComputer interface — called by ComputerTool after each model   #
    # action. The model sends coordinates derived from the last screenshot.#
    # ------------------------------------------------------------------ #

    async def screenshot(self) -> str:
        """Return a base64-encoded PNG of the current viewport."""
        # ComputerTool repeatedly alternates between:
        #   1. ask this object for a screenshot,
        #   2. let the model choose the next UI action,
        #   3. call one of the action methods below,
        #   4. request another screenshot.
        #
        # The SDK expects the screenshot as a base64 string, not raw bytes.
        # `full_page=False` captures only the visible viewport, which is the
        # coordinate system used for mouse actions.
        png_bytes = await self.page.screenshot(full_page=False)
        return base64.b64encode(png_bytes).decode('utf-8')

    def normalize_keys(self, keys: list[str] | None) -> list[str]:
        """Translate model-facing key names to Playwright key names."""
        # The model may request keys in a compact, user-facing form. Any key we
        # do not recognize is passed through unchanged, which lets Playwright
        # handle keys it already knows about.
        return [KEY_MAP.get(k.lower(), k) for k in (keys or [])]

    @asynccontextmanager
    async def hold_keys(self, keys: list[str] | None) -> AsyncIterator[None]:
        """Hold modifier keys (Ctrl, Shift, …) during a mouse action."""
        # Some computer actions include modifier keys. For example, the model
        # may request Ctrl+click or Shift+click. Playwright models that as:
        # press the modifier down, perform the mouse action, release it.
        mapped = self.normalize_keys(keys)
        try:
            for k in mapped:
                await self.page.keyboard.down(k)
            yield
        finally:
            # Release keys in reverse order. This mirrors how users release key
            # chords and avoids leaving a modifier key logically pressed if the
            # action raises an exception.
            for k in reversed(mapped):
                await self.page.keyboard.up(k)

    async def click(
        self, x: int, y: int, button: Button = 'left',
        *, keys: list[str] | None = None,
    ) -> None:
        # The model chooses x/y coordinates from the most recent screenshot.
        # Playwright expects a known mouse-button string, so normalize anything
        # unexpected to a left click for safety.
        btn: Literal['left', 'middle', 'right'] = (
            button if button in ('left', 'middle', 'right') else 'left'
        )
        async with self.hold_keys(keys):
            await self.page.mouse.click(x, y, button=btn)

    async def double_click(
        self, x: int, y: int, *, keys: list[str] | None = None,
    ) -> None:
        # Double-click is rarely needed for websites, but the AsyncComputer
        # interface includes it and some model plans may request it.
        async with self.hold_keys(keys):
            await self.page.mouse.dblclick(x, y)

    async def scroll(
        self, x: int, y: int, scroll_x: int, scroll_y: int,
        *, keys: list[str] | None = None,
    ) -> None:
        # The model supplies an anchor point plus horizontal/vertical scroll
        # deltas. We move the mouse to the anchor point so the action resembles
        # a normal browser scroll, then scroll the page with JavaScript.
        async with self.hold_keys(keys):
            await self.page.mouse.move(x, y)
            await self.page.evaluate(f'window.scrollBy({scroll_x}, {scroll_y})')

    async def type(self, text: str) -> None:
        # Text is typed into whichever element currently has focus. The model
        # usually focuses a search box or form field with a prior click action.
        await self.page.keyboard.type(text)

    async def wait(self) -> None:
        # Many web pages update asynchronously after a click, search or scroll.
        # A short wait gives the next screenshot a better chance of reflecting
        # the result of the previous action.
        await asyncio.sleep(1)

    async def move(
        self, x: int, y: int, *, keys: list[str] | None = None,
    ) -> None:
        # Move is useful for hover menus and for positioning the cursor before
        # another action. It does not click or type by itself.
        async with self.hold_keys(keys):
            await self.page.mouse.move(x, y)

    async def keypress(self, keys: list[str]) -> None:
        # `keys` may represent a chord, such as ["ctrl", "l"], or a simple key,
        # such as ["enter"]. Press all keys down first, then release them in
        # reverse order to emulate a real keyboard shortcut.
        mapped_keys = self.normalize_keys(keys)
        for key in mapped_keys:
            await self.page.keyboard.down(key)
        for key in reversed(mapped_keys):
            await self.page.keyboard.up(key)

    async def drag(
        self, path: list[tuple[int, int]], *, keys: list[str] | None = None,
    ) -> None:
        # Drag receives a path of screen coordinates. The first point presses
        # the mouse button, intermediate points move the cursor, and the final
        # point releases the button. Weather pages rarely need this, but keeping
        # the method makes the computer implementation complete.
        if not path:
            return
        async with self.hold_keys(keys):
            await self.page.mouse.move(path[0][0], path[0][1])
            await self.page.mouse.down()
            for px, py in path[1:]:
                await self.page.mouse.move(px, py)
            await self.page.mouse.up()
