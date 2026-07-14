"""Unit tests for the Browser class."""

from unittest.mock import patch

from src.omnitest.browser import Browser


@patch("omnitest.browser.browser.sync_playwright")
def test_browser_start(_sync):
    """Verify that Browser starts successfully during initialization."""
    browser = Browser()

    assert browser.started