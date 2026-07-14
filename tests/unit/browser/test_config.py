from omnitest.browser import BrowserConfig


def test_default_headless():

    config = BrowserConfig()

    assert config.headless is True


def test_default_browser():

    config = BrowserConfig()

    assert config.browser == "chromium"