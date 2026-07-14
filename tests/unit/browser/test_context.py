from unittest.mock import MagicMock

from omnitest.browser.context import BrowserContext
from omnitest.browser.page import PageManager


def test_browser_reference():
    browser = MagicMock()
    context = MagicMock()

    browser_context = BrowserContext(browser, context)

    assert browser_context.browser == browser


def test_context_reference():
    browser = MagicMock()
    context = MagicMock()

    browser_context = BrowserContext(browser, context)

    assert browser_context._context == context


def test_page_manager_created():
    browser = MagicMock()
    context = MagicMock()

    browser_context = BrowserContext(browser, context)

    assert isinstance(browser_context.page, PageManager)
