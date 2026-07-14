"""Browser SDK for OmniTest.

This module provides the Browser class, which is the main entry point for
browser automation. It manages the Playwright lifecycle, browser launch,
browser context, and delegates page operations to PageManager.
"""

from __future__ import annotations

from typing import Optional

try:
    from playwright.sync_api import (
        Browser as PlaywrightBrowser,
        BrowserContext,
        Playwright,
        sync_playwright,
    )
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    PlaywrightBrowser = object
    BrowserContext = object
    Playwright = object

    def sync_playwright():
        raise RuntimeError("playwright is not installed")

from .config import BrowserConfig
from .page import PageManager
from omnitest.actions.click import ClickAction
from omnitest.actions.fill import FillAction


class Browser:
    """
    Main browser interface for OmniTest.
    """

    def __init__(
        self,
        config: BrowserConfig | None = None,
        **overrides,
    ) -> None:
        """
        Initialize a browser session.

        Parameters
        ----------
        config:
            Browser configuration.

        overrides:
            Override any BrowserConfig property.

            Example
            -------
            Browser(headless=False)

            Browser(browser="firefox")
        """

        self.config = config or BrowserConfig()

        for key, value in overrides.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)
            else:
                raise AttributeError(
                    f"Unknown browser configuration '{key}'"
                )

        self._playwright: Optional[Playwright] = None
        self._browser: Optional[PlaywrightBrowser] = None
        self._context: Optional[BrowserContext] = None

        self.page: Optional[PageManager] = None

        self._started = False

        self.start()
        
    # ----------------------------------------------------- #
    # Browser Lifecycle
    # ----------------------------------------------------- #

    def start(self) -> None:
        """
        Launch browser.

        Safe to call multiple times.
        """

        if self._started:
            return

        self._playwright = sync_playwright().start()

        launcher = getattr(
            self._playwright,
            self.config.browser,
        )

        self._browser = launcher.launch(**self.config.launch_options)

        self._context = self._browser.new_context(**self.config.context_options)

        self.page = PageManager(self._context)

        self._click = ClickAction(self._browser)
        self._fill = FillAction(self._browser)
        
        self._started = True

    # ----------------------------------------------------- #

    @property
    def started(self) -> bool:
        """Return whether the browser session has been started."""
        return self._started

    def close(self) -> None:
        """
        Close browser and cleanup resources.
        """

        if self._context:
            self._context.close()

        if self._browser:
            self._browser.close()

        if self._playwright:
            self._playwright.stop()

        self._started = False

    # ----------------------------------------------------- #
    # Navigation
    # ----------------------------------------------------- #

    def open(self, url: str):
        """
        Open URL.
        """

        self.page.goto(url)

    # ----------------------------------------------------- #

    @property
    def current_page(self):
        """
        Return active Playwright page.
        """

        return self.page.current


    # ----------------------------------------------------- #
    # Context Manager
    # ----------------------------------------------------- #

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()        
        
    # ------------------------------------------------------------------ #
    # Actions
    # ------------------------------------------------------------------ #

    def click(self, selector: str) -> None:
        """
        Click an element.
        """
        self._click(selector)


    def type(self, selector: str, text: str) -> None:
        """
        Type text into an element.
        """
        self._fill(selector, text)