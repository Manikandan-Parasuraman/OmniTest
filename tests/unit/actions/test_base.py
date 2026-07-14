"""Unit tests for the BaseAction class."""

from unittest.mock import MagicMock

from src.omnitest.actions.base import BaseAction


def test_base_action_initialization():
    """Verify that BaseAction stores the provided browser instance."""
    browser = MagicMock()

    action = BaseAction(browser)

    assert action.browser == browser


def test_playwright_property():
    """Verify that the playwright property returns the browser's Playwright page instance."""
    browser = MagicMock()
    page = MagicMock()

    browser.page.playwright = page

    action = BaseAction(browser)

    assert action.playwright == page
