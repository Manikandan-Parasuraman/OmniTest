import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_browser():
    """Provide a mock browser with a mocked Playwright page for unit tests."""

    browser = MagicMock()
    browser.page.playwright = MagicMock()
    return browser


@pytest.fixture
def mock_locator():
    """Provide a mock Playwright locator for action and locator tests."""

    return MagicMock()