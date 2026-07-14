"""Locator utilities: selector types, parser, and engine.

This package provides a small selector DSL and helpers to convert user
selectors into Playwright locators.
"""

from .selector import Selector
from .parser import SelectorParser
from .engine import LocatorEngine

__all__ = [
    "Selector",
    "SelectorParser",
    "LocatorEngine",
]
