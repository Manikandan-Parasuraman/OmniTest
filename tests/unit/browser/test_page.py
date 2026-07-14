# tests/unit/locator/test_parser.py

import pytest

from omnitest.locator import SelectorParser


def test_parse_css_selector():
    selector = SelectorParser.parse("#login")

    assert selector.strategy == "css"
    assert selector.value == "#login"


def test_parse_xpath():
    selector = SelectorParser.parse("//button")

    assert selector.strategy == "xpath"


def test_parse_text():
    selector = SelectorParser.parse("Login")

    assert selector.strategy == "text"


def test_empty_selector():
    with pytest.raises(ValueError):
        SelectorParser.parse("")


def test_invalid_type():
    with pytest.raises(TypeError):
        SelectorParser.parse(123)
