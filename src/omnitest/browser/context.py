"""
Browser context implementation for OmniTest.

This module provides the BrowserContext abstraction responsible for
creating and managing Playwright browser contexts.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

try:
    from playwright.sync_api import (
        Browser as PlaywrightBrowser,
        BrowserContext as PlaywrightContext,
        Error as PlaywrightError,
    )
except ModuleNotFoundError:  # pragma: no cover
    PlaywrightBrowser = Any
    PlaywrightContext = Any
    PlaywrightError = Exception

from omnitest.logger import get_logger
from omnitest.exceptions import ContextCreationError

from .config import BrowserConfig
from .page import PageManager

if TYPE_CHECKING:
    from .page import BrowserPage

logger = get_logger(__name__)


class BrowserContext:
    """
    OmniTest Browser Context.

    This class owns the Playwright BrowserContext and manages all pages
    created within it.

    Parameters
    ----------
    browser:
        Playwright browser instance.

    config:
        Browser configuration.
    """

    def __init__(
        self,
        browser: PlaywrightBrowser,
        config: BrowserConfig | PlaywrightContext,
    ) -> None:

        self.browser = browser
        self._browser = browser
        self._config = config

        self._context: PlaywrightContext | None = None

        self.page = None

        if isinstance(config, BrowserConfig):
            self._create_context()
        else:
            self._context = config
            self.page = PageManager(self._context)

    # ------------------------------------------------------------------ #
    # Internal
    # ------------------------------------------------------------------ #

    def _create_context(self) -> None:
        """
        Create Playwright browser context.
        """

        try:

            logger.info("Creating browser context")

            self._context = self._browser.new_context(
                **self._config.context_options
            )

            self._context.set_default_timeout(
                self._config.timeout
            )

            self._context.set_default_navigation_timeout(
                self._config.navigation_timeout
            )

            self.page = PageManager(self._context)

            logger.info("Browser context created")

        except PlaywrightError as exc:
            raise ContextCreationError(str(exc)) from exc

    # ------------------------------------------------------------------ #
    # Properties
    # ------------------------------------------------------------------ #

    @property
    def playwright(self) -> PlaywrightContext:
        """
        Return the underlying Playwright context.

        Internal framework use only.
        """
        return self._context

    # ------------------------------------------------------------------ #
    # Cookies
    # ------------------------------------------------------------------ #

    def cookies(self) -> list[dict]:
        """
        Return browser cookies.
        """
        return self._context.cookies()

    def clear_cookies(self) -> None:
        """
        Remove all cookies.
        """
        self._context.clear_cookies()

    def add_cookies(
        self,
        cookies: list[dict],
    ) -> None:
        """
        Add cookies.
        """
        self._context.add_cookies(cookies)

    # ------------------------------------------------------------------ #
    # Storage
    # ------------------------------------------------------------------ #

    def storage_state(
        self,
        path: str | None = None,
    ) -> dict:
        """
        Return or save storage state.
        """

        return self._context.storage_state(
            path=path,
        )

    # ------------------------------------------------------------------ #
    # Pages
    # ------------------------------------------------------------------ #

    def new_page(self) -> "BrowserPage":
        """
        Create a new browser page.
        """

        return self.page.new_page()

    @property
    def pages(self):
        """
        Return all open pages.
        """

        return self.page.pages

    # ------------------------------------------------------------------ #
    # Close
    # ------------------------------------------------------------------ #

    def close(self) -> None:
        """
        Close browser context.
        """

        if self._context:

            logger.info("Closing browser context")

            self._context.close()

            logger.info("Browser context closed")
            
            
    def __getattr__(self, name: str):
        return getattr(self.page.current, name)