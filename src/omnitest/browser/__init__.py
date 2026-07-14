"""Browser abstractions for omnitest."""

from .browser import Browser
from .context import BrowserContext
from .page import Page
from .config import BrowserConfig, BrowserType, ColorScheme

__all__ = ["Browser", "BrowserContext", "Page", "BrowserConfig", "BrowserType", "ColorScheme"]
