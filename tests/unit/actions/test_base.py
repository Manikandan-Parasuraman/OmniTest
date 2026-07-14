from unittest.mock import MagicMock

from omnitest.actions.base import BaseAction


def test_base_action_initialization():

    browser = MagicMock()

    action = BaseAction(browser)

    assert action.browser == browser


def test_playwright_property():

    browser = MagicMock()

    page = MagicMock()

    browser.page.playwright = page

    action = BaseAction(browser)

    assert action.playwright == page