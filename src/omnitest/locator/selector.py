from dataclasses import dataclass
from typing import Any, Literal

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