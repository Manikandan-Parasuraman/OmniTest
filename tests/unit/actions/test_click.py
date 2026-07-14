from unittest.mock import MagicMock

from omnitest.actions.click import ClickAction


def test_click(mock_browser):
    """Verify that ClickAction clicks the element matching the given selector."""

    action = ClickAction(mock_browser)

    action("#login")

    mock_browser.page.playwright.locator.return_value.click.assert_called_once()