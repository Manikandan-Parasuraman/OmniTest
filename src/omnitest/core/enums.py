"""Enumerations used by the core OmniTest package."""

from enum import Enum


class BrowserType(Enum):
    """Supported browser engine identifiers."""

    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"
