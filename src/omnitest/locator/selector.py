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
    """
    Normalized selector representation.
    """

    strategy: SelectorType
    value: Any