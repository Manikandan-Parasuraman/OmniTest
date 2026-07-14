"""Unit tests for the SelectorParser class."""

import pytest

from src.omnitest.locator import SelectorParser


def test_parse_css_selector():
    """Verify that a CSS selector is parsed with the 'css' strategy."""
    selector = SelectorParser.parse("#login")

    assert selector.strategy == "css"
    assert selector.value == "#login"


def test_parse_xpath():
    """Verify that an XPath selector is parsed with the 'xpath' strategy."""
    selector = SelectorParser.parse("//button")

    assert selector.strategy == "xpath"


def test_parse_text():
    """Verify that plain text is parsed with the 'text' strategy."""
    selector = SelectorParser.parse("Login")

    assert selector.strategy == "text"


def test_empty_selector():
    """Verify that parsing an empty selector raises a ValueError."""
    with pytest.raises(ValueError):
        SelectorParser.parse("")


def test_invalid_type():
    """Verify that parsing a non-string selector raises a TypeError."""
    with pytest.raises(TypeError):
        SelectorParser.parse(123)