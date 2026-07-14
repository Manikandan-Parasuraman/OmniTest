"""Selector types and helper dataclasses for selector normalization.

This module declares supported selector strategies and the `Selector`
dataclass used by the `SelectorParser` and `LocatorEngine`.
"""

from dataclasses import dataclass
from typing import Any, Literal

SUPPORTED_SELECTOR_STRATEGIES = {
    "css",
    "xpath",
    "text",
    "role",
    "label",
    "placeholder",
    "testid",
    "alt",
    "title",
}

SelectorType = Literal[
    "css",
    "xpath",
    "text",
    "role",
    "label",
    "placeholder",
    "testid",
    "alt",
    "title",
]


@dataclass(slots=True, frozen=True)
class Selector:
    """Normalized selector representation.

    Attributes
    ----------
    strategy:
        The selector strategy string (one of the supported strategies).
    value:
        The selector value; type depends on the strategy.
    """

    strategy: SelectorType
    value: Any
