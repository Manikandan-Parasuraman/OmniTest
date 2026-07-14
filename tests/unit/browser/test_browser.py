from unittest.mock import patch

from omnitest.browser import Browser


@patch("omnitest.browser.browser.sync_playwright")
def test_browser_start(sync):
    """Verify that Browser starts successfully during initialization."""

    browser = Browser()

    assert browser.started