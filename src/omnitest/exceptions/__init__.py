"""Exception definitions for omnitest."""

from .browser import (
    BrowserConnectionError,
    BrowserNotInitializedError,
    ContextCreationError,
    OmniTestBrowserError,
    PageCreationError,
)

__all__ = [
    "OmniTestBrowserError",
    "BrowserNotInitializedError",
    "BrowserConnectionError",
    "PageCreationError",
    "ContextCreationError",
]
