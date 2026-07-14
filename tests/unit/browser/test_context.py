from unittest.mock import MagicMock

from omnitest.browser.context import BrowserContext
from omnitest.browser.page import PageManager


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

    assert browser_context._context == context


def test_page_manager_created():
    """Verify that BrowserContext initializes a PageManager instance."""

    browser = MagicMock()
    context = MagicMock()

    browser_context = BrowserContext(browser, context)

    assert isinstance(browser_context.page, PageManager)