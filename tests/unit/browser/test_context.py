"""Unit tests for the BrowserContext class."""

from unittest.mock import MagicMock

from src.omnitest.browser.context import BrowserContext
from src.omnitest.browser.page import PageManager


def test_browser_reference():
    """Verify that BrowserContext stores the provided browser instance."""
    browser = MagicMock()
    context = MagicMock()

    browser_context = BrowserContext(browser, context)

    assert browser_context.browser == browser


def test_context_reference():
    """Verify that BrowserContext stores the provided Playwright browser context."""
    browser = MagicMock()
    context = MagicMock()

    browser_context = BrowserContext(browser, context)

    assert browser_context._context == context  # pylint: disable=protected-access


def test_page_manager_created():
    """Verify that BrowserContext initializes a PageManager instance."""
    browser = MagicMock()
    context = MagicMock()

    browser_context = BrowserContext(browser, context)

    assert isinstance(browser_context.page, PageManager)
