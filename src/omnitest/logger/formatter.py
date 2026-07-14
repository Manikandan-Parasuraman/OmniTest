"""Formatting helpers for omnitest logs."""

from __future__ import annotations

import logging


class OmnitestFormatter(logging.Formatter):
    """A simple formatter used by the omnitest logger."""

    def __init__(self, fmt: str = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s") -> None:
        super().__init__(fmt=fmt)
