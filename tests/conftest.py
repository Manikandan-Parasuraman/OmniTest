import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_browser():
    browser = MagicMock()
    browser.page.playwright = MagicMock()
    return browser


@pytest.fixture
def mock_locator():
    return MagicMock()
