"""
Base action implementation for OmniTest.

All browser actions inherit from BaseAction.

Responsibilities
----------------
- Access current browser page
- Create Playwright locators
- Common logging
- Shared validation
- Foundation for retries and reporting
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

try:
    from playwright.sync_api import Locator
except ModuleNotFoundError:  # pragma: no cover
    Locator = Any

from omnitest.logger import get_logger
from collections.abc import Callable
from typing import Any  # noqa: F821
from omnitest.locator.engine import LocatorEngine


if TYPE_CHECKING:
    from omnitest.browser.page import BrowserPage

logger = get_logger(__name__)


class BaseAction:
    """
    Base class for all browser actions.

    Parameters
    ----------
    page:
        Active BrowserPage instance.
    """

    def __init__(self, browser) -> None:
        self.browser = browser

    # ------------------------------------------------------------------ #
    # Properties
    # ------------------------------------------------------------------ #

    @property
    def page(self) -> "BrowserPage":
        """
        Return the current BrowserPage.
        """
        return self.browser.page

    @property
    def playwright(self):
        """
        Return the active Playwright page.

        This always points to the current browser page, even after
        switching tabs or opening new pages.
        """
        return self.browser.page.playwright

    # ------------------------------------------------------------------ #
    # Locator Helpers
    # ------------------------------------------------------------------ #

    def locator(self, selector):
        """
        Resolve a selector into a Playwright Locator.
        """
        return LocatorEngine(self.playwright).find(selector)

    # ------------------------------------------------------------------ #
    # Logging
    # ------------------------------------------------------------------ #

    def log(self, message: str, *args) -> None:
        """
        Write an action log message.
        """
        logger.info(message, *args)

    # ------------------------------------------------------------------ #
    # Validation
    # ------------------------------------------------------------------ #

    @staticmethod
    def validate_selector(selector: str) -> None:
        """
        Validate selector input.
        """
        if not isinstance(selector, str):
            raise TypeError("Selector must be a string.")

        if not selector.strip():
            raise ValueError("Selector cannot be empty.")

    # ------------------------------------------------------------------ #
    # Future Extension Points
    # ------------------------------------------------------------------ #

    def before_action(self, action: str) -> None:
        """
        Hook executed before every action.

        Future use:
        - Highlight element
        - Start timer
        - Reporting
        """
        logger.debug("Starting action: %s", action)

    def after_action(self, action: str) -> None:
        """
        Hook executed after every action.

        Future use:
        - Stop timer
        - Reporting
        """
        logger.debug("Completed action: %s", action)

    def on_error(self, action: str, exc: Exception) -> None:
        """
        Hook executed when an action fails.

        Future use:
        - Screenshot
        - Retry
        - HTML report
        """
        logger.exception("Action '%s' failed: %s", action, exc)
        
    def execute(
        self,
        action: str,
        func: Callable[..., Any],
        *args,
        **kwargs,
    ) -> Any:
        """
        Execute a browser action with common logging and error handling.
        """

        self.before_action(action)

        try:
            result = func(*args, **kwargs)

            self.after_action(action)

            return result

        except Exception as exc:
            self.on_error(action, exc)
            raise  # noqa: F401