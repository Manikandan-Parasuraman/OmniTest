"""Unit tests for the BrowserConfig class."""

from omnitest.browser import BrowserConfig


def test_default_headless():
    """Verify that BrowserConfig enables headless mode by default."""
    config = BrowserConfig()

    assert config.headless is True


def test_default_browser():
    """Verify that BrowserConfig uses Chromium as the default browser."""
    config = BrowserConfig()

    assert config.browser == "chromium"
