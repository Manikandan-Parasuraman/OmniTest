from unittest.mock import MagicMock

from omnitest.locator import LocatorEngine


def test_css_locator():
    """Verify that a CSS selector is resolved using page.locator()."""

    page = MagicMock()

    LocatorEngine(page).find("#login")

    page.locator.assert_called_once_with("#login")


def test_text_locator():
    """Verify that a text selector is resolved using page.get_by_text()."""

    page = MagicMock()

    LocatorEngine(page).find("Login")

    page.get_by_text.assert_called_once_with("Login")