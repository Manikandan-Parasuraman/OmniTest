"""Action helpers for browser automation."""

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
