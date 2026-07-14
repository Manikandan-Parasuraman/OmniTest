from typing import get_args

import pytest

from omnitest.locator.parser import SelectorParser
from omnitest.locator.selector import SUPPORTED_SELECTOR_STRATEGIES, Selector, SelectorType


# --------------------------------------------------------------------
# String Selectors
# --------------------------------------------------------------------

def test_parse_css_id_selector():
    """Verify that a CSS ID selector is parsed using the 'css' strategy."""

    selector = SelectorParser.parse("#login")

    assert selector.strategy == "css"
    assert selector.value == "#login"


def test_parse_css_class_selector():
    """Verify that a CSS class selector is parsed using the 'css' strategy."""

    selector = SelectorParser.parse(".button")

    assert selector.strategy == "css"
    assert selector.value == ".button"


def test_parse_css_attribute_selector():
    """Verify that a CSS attribute selector is parsed using the 'css' strategy."""

    selector = SelectorParser.parse("[data-testid='submit']")

    assert selector.strategy == "css"
    assert selector.value == "[data-testid='submit']"


def test_parse_css_prefix():
    """Verify that selectors prefixed with 'css=' are parsed correctly."""

    selector = SelectorParser.parse("css=#login")

    assert selector.strategy == "css"
    assert selector.value == "#login"


def test_parse_xpath():
    """Verify that an XPath selector is parsed using the 'xpath' strategy."""

    selector = SelectorParser.parse("//button")

    assert selector.strategy == "xpath"
    assert selector.value == "//button"


def test_parse_xpath_prefix():
    """Verify that selectors prefixed with 'xpath=' are parsed correctly."""

    selector = SelectorParser.parse("xpath=//button")

    assert selector.strategy == "xpath"
    assert selector.value == "//button"


def test_parse_text():
    """Verify that plain text is parsed using the 'text' strategy."""

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
    """Verify that tuple-based selectors are parsed using the provided strategy."""

    selector = SelectorParser.parse((strategy, value))

    assert selector.strategy == strategy
    assert selector.value == value


def test_supported_selector_strategies_are_shared():
    """Verify that the supported selector strategies match the SelectorType definition."""

    expected = set(get_args(SelectorType))

    assert SUPPORTED_SELECTOR_STRATEGIES == expected


# --------------------------------------------------------------------
# Dictionary Selectors
# --------------------------------------------------------------------

def test_parse_role_dictionary():
    """Verify that role-based dictionary selectors preserve role and keyword arguments."""

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
    """Verify that parsing an existing Selector returns the same object."""

    selector = Selector("css", "#login")

    parsed = SelectorParser.parse(selector)

    assert parsed is selector


# --------------------------------------------------------------------
# Invalid Inputs
# --------------------------------------------------------------------

def test_empty_selector():
    """Verify that an empty selector raises a ValueError."""

    with pytest.raises(ValueError):
        SelectorParser.parse("")


def test_blank_selector():
    """Verify that a blank selector raises a ValueError."""

    with pytest.raises(ValueError):
        SelectorParser.parse("   ")


def test_invalid_selector_type():
    """Verify that unsupported selector types raise a TypeError."""

    with pytest.raises(TypeError):
        SelectorParser.parse(123)


def test_invalid_tuple_length():
    """Verify that tuples with an invalid number of elements raise a ValueError."""

    with pytest.raises(ValueError):
        SelectorParser.parse(("css", "#login", "extra"))


def test_invalid_strategy():
    """Verify that unsupported selector strategies raise a ValueError."""

    with pytest.raises(ValueError):
        SelectorParser.parse(("invalid", "value"))


def test_invalid_dictionary():
    """Verify that dictionaries without a valid selector strategy raise a ValueError."""

    with pytest.raises(ValueError):
        SelectorParser.parse({"name": "Login"})