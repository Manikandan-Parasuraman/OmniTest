"""
Page management for OmniTest.

This module provides BrowserPage and PageManager, which wrap Playwright
pages and manage browser tabs.
"""

# Allow Playwright aliases that look like constants
# pylint: disable=invalid-name

from __future__ import annotations

from typing import Any

try:
    from playwright.sync_api import (
        BrowserContext as PlaywrightContext,
        Page as PlaywrightPage,
        Error as PlaywrightError,
    )
except ModuleNotFoundError:  # pragma: no cover
    PlaywrightContext = Any
    PlaywrightPage = Any
    PlaywrightError = Exception

from omnitest.logger import get_logger
from omnitest.exceptions import PageCreationError

logger = get_logger(__name__)


class BrowserPage:
    """
    OmniTest wrapper around a Playwright Page.

    Users never interact with Playwright directly.
    """

    def __init__(self, page: PlaywrightPage) -> None:
        self._page = page

    # ------------------------------------------------------------------ #
    # Properties
    # ------------------------------------------------------------------ #

    @property
    def playwright(self) -> PlaywrightPage:
        """
        Internal access to Playwright page.

        Framework code should use this when direct Playwright APIs are
        required.
        """
        return self._page

    @property
    def url(self) -> str:
        """Return current page URL."""
        return self._page.url

    @property
    def title(self) -> str:
        """Return page title."""
        return self._page.title()

    # ------------------------------------------------------------------ #
    # Navigation
    # ------------------------------------------------------------------ #

    def goto(self, url: str, **kwargs):
        """Navigate to `url` using the Playwright page."""
        logger.info("Navigate -> %s", url)
        return self._page.goto(url, **kwargs)

    def reload(self):
        """Reload the current page."""
        logger.info("Reload page")
        return self._page.reload()

    def back(self):
        """Navigate back in browser history."""
        logger.info("Navigate back")
        return self._page.go_back()

    def forward(self):
        """Navigate forward in browser history."""
        logger.info("Navigate forward")
        return self._page.go_forward()

    def close(self):
        """Close the underlying Playwright page."""
        logger.info("Closing page")
        self._page.close()

    # ------------------------------------------------------------------ #
    # Internal delegation
    # ------------------------------------------------------------------ #

    def __getattr__(self, name: str):
        """
        Delegate unknown APIs to Playwright.

        This allows OmniTest internals to access Playwright APIs without
        exposing Playwright in the public API.
        """
        return getattr(self._page, name)


Page = BrowserPage


class PageManager:
    """
    Manage browser pages (tabs).
    """

    def __init__(self, context: PlaywrightContext) -> None:

        self._context = context

        self._pages: list[BrowserPage] = []

        self._current: BrowserPage | None = None

        self.new_page()

    # ------------------------------------------------------------------ #
    # Properties
    # ------------------------------------------------------------------ #

    @property
    def current(self) -> BrowserPage:
        """
        Return active page.
        """
        return self._current

    @property
    def pages(self) -> list[BrowserPage]:
        """
        Return all open pages.
        """
        return self._pages

    @property
    def count(self) -> int:
        """
        Number of open pages.
        """
        return len(self._pages)

    # ------------------------------------------------------------------ #
    # Page Management
    # ------------------------------------------------------------------ #

    def new_page(self) -> BrowserPage:
        """
        Create a new browser tab.
        """

        try:

            logger.info("Creating new page")

            page = BrowserPage(
                self._context.new_page()
            )

            self._pages.append(page)

            self._current = page

            return page

        except PlaywrightError as exc:
            raise PageCreationError(str(exc)) from exc

    def switch(self, index: int) -> BrowserPage:
        """
        Switch active page.
        """

        self._current = self._pages[index]

        logger.info("Switched to page %s", index)

        return self._current

    def close_current(self) -> None:
        """
        Close active page.
        """

        if self._current is None:
            return

        self._current.close()

        self._pages.remove(self._current)

        if self._pages:
            self._current = self._pages[-1]
        else:
            self._current = None

    def close_all(self) -> None:
        """
        Close all browser pages.
        """

        for page in list(self._pages):
            page.close()

        self._pages.clear()

        self._current = None

    # ------------------------------------------------------------------ #
    # Navigation
    # ------------------------------------------------------------------ #

    def goto(self, url: str):
        """Navigate active page to `url`."""
        return self.current.goto(url)

    def reload(self):
        """Reload the active page."""
        return self.current.reload()

    def back(self):
        """Navigate back on the active page."""
        return self.current.back()

    def forward(self):
        """Navigate forward on the active page."""
        return self.current.forward()

    # ------------------------------------------------------------------ #
    # Delegation
    # ------------------------------------------------------------------ #

    def __getattr__(self, name: str):
        """
        Delegate unknown attributes to the active BrowserPage.
        """
        return getattr(self.current, name)
