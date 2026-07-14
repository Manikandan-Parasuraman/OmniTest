"""
Selector parser for OmniTest.

This module parses user-provided selectors into a normalized format
that can be consumed by the LocatorEngine.
"""

from __future__ import annotations

from typing import Any

from .selector import SUPPORTED_SELECTOR_STRATEGIES, Selector


class SelectorParser:   # pylint: disable=too-few-public-methods
    """
    Parse user selectors into a normalized Selector object.

    Supported formats
    -----------------

    CSS
    ----
    "#login"
    ".button"
    "input[name='username']"

    XPath
    ------
    "//button"
    "(//button)[1]"

    Text
    ----
    "Login"

    Tuple
    -----
    ("role", "button")
    ("label", "Username")
    ("placeholder", "Search")
    ("testid", "submit-btn")

    Dictionary
    ----------
    {
        "role": "button",
        "name": "Login"
    }
    """

    @classmethod
    def parse(cls, selector: Any) -> Selector:
        """
        Parse any supported selector.
        """

        if isinstance(selector, Selector):
            return selector

        if isinstance(selector, str):
            return cls._parse_string(selector)

        if isinstance(selector, tuple):
            return cls._parse_tuple(selector)

        if isinstance(selector, dict):
            return cls._parse_dict(selector)

        raise TypeError(
            f"Unsupported selector type: {type(selector).__name__}"
        )

    # ------------------------------------------------------------------ #

    @staticmethod
    def _parse_string(selector: str) -> Selector:

        selector = selector.strip()

        if not selector:
            raise ValueError("Selector cannot be empty.")

        # XPath
        if selector.startswith("//") or selector.startswith("(//"):
            return Selector("xpath", selector)

        # Explicit Playwright syntax
        if selector.startswith("xpath="):
            return Selector("xpath", selector[6:])

        if selector.startswith("css="):
            return Selector("css", selector[4:])

        # CSS
        if (
            selector.startswith("#")
            or selector.startswith(".")
            or selector.startswith("[")
        ):
            return Selector("css", selector)

        # Default = visible text
        return Selector("text", selector)

    # ------------------------------------------------------------------ #

    @staticmethod
    def _parse_tuple(selector: tuple) -> Selector:

        if len(selector) != 2:
            raise ValueError(
                "Tuple selector must contain exactly two values."
            )

        strategy, value = selector

        strategy = strategy.lower()

        if strategy not in SUPPORTED_SELECTOR_STRATEGIES:
            raise ValueError(
                f"Unsupported selector strategy '{strategy}'."
            )

        return Selector(strategy, value)

    # ------------------------------------------------------------------ #

    @staticmethod
    def _parse_dict(selector: dict) -> Selector:
        """
        Parse dictionary selectors.

        Example
        -------
        {
            "role": "button",
            "name": "Login"
        }
        """

        if "role" in selector:

            role = selector["role"]

            kwargs = {
                key: value
                for key, value in selector.items()
                if key != "role"
            }

            return Selector(
                "role",
                (role, kwargs),
            )

        raise ValueError(
            "Unsupported dictionary selector."
        )
