"""Action helpers for browser automation."""

# Allow lowercase aliases for convenience (they reference action classes)
# pylint: disable=invalid-name

from .click import ClickAction
from .fill import FillAction
from .hover import HoverAction

click = ClickAction
fill = FillAction
hover = HoverAction

__all__ = [
    "ClickAction",
    "FillAction",
    "HoverAction",
    "click",
    "fill",
    "hover",
]
