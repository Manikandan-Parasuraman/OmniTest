from typing import get_args

import pytest

from omnitest.locator.parser import SelectorParser
from omnitest.locator.selector import SUPPORTED_SELECTOR_STRATEGIES, Selector, SelectorType


# --------------------------------------------------------------------
# String Selectors
# --------------------------------------------------------------------

def test_parse_css_id_selector():
    selector = SelectorParser.parse("#login")

    assert selector.strategy == "css"
    assert selector.value == "#login"


def test_parse_css_class_selector():
    selector = SelectorParser.parse(".button")

    assert selector.strategy == "css"
    assert selector.value == ".button"


def test_parse_css_attribute_selector():
    selector = SelectorParser.parse("[data-testid='submit']")

    assert selector.strategy == "css"
    assert selector.value == "[data-testid='submit']"


def test_parse_css_prefix():
    selector = SelectorParser.parse("css=#login")

    assert selector.strategy == "css"
    assert selector.value == "#login"


def test_parse_xpath():
    selector = SelectorParser.parse("//button")

    assert selector.strategy == "xpath"
    assert selector.value == "//button"


def test_parse_xpath_prefix():
    selector = SelectorParser.parse("xpath=//button")

    assert selector.strategy == "xpath"
    assert selector.value == "//button"


def test_parse_text():
    selector = SelectorParser.parse("Login")

    assert selector.strategy == "text"
    assert selector.value == "Login"


# --------------------------------------------------------------------
# Tuple Selectors
# --------------------------------------------------------------------

@pytest.mark.parametrize(
    "strategy,value",
    [
        ("role", "button"),
        ("label", "Username"),
        ("placeholder", "Search"),
        ("testid", "submit"),
        ("alt", "Company Logo"),
        ("title", "Close"),
        ("css", "#login"),
        ("xpath", "//button"),
        ("text", "Login"),
    ],
)
def test_parse_tuple(strategy, value):
    selector = SelectorParser.parse((strategy, value))

    assert selector.strategy == strategy
    assert selector.value == value


def test_supported_selector_strategies_are_shared():
    expected = set(get_args(SelectorType))

    assert SUPPORTED_SELECTOR_STRATEGIES == expected


# --------------------------------------------------------------------
# Dictionary Selectors
# --------------------------------------------------------------------

def test_parse_role_dictionary():
    selector = SelectorParser.parse(
        {
            "role": "button",
            "name": "Login",
            "exact": True,
        }
    )

    assert selector.strategy == "role"

    role, kwargs = selector.value

    assert role == "button"
    assert kwargs["name"] == "Login"
    assert kwargs["exact"] is True


# --------------------------------------------------------------------
# Existing Selector Object
# --------------------------------------------------------------------

def test_existing_selector_returns_same_instance():
    selector = Selector("css", "#login")

    parsed = SelectorParser.parse(selector)

    assert parsed is selector


# --------------------------------------------------------------------
# Invalid Inputs
# --------------------------------------------------------------------

def test_empty_selector():
    with pytest.raises(ValueError):
        SelectorParser.parse("")


def test_blank_selector():
    with pytest.raises(ValueError):
        SelectorParser.parse("   ")


def test_invalid_selector_type():
    with pytest.raises(TypeError):
        SelectorParser.parse(123)


def test_invalid_tuple_length():
    with pytest.raises(ValueError):
        SelectorParser.parse(("css", "#login", "extra"))


def test_invalid_strategy():
    with pytest.raises(ValueError):
        SelectorParser.parse(("invalid", "value"))


def test_invalid_dictionary():
    with pytest.raises(ValueError):
        SelectorParser.parse({"name": "Login"})