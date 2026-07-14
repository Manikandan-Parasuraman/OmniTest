"""Browser-related exceptions."""


class OmniTestBrowserError(Exception):
    """Base exception for browser-related failures."""


class BrowserNotInitializedError(OmniTestBrowserError):
    """Raised when a browser context or page is requested before initialization."""


class BrowserConnectionError(OmniTestBrowserError):
    """Raised when the browser cannot be started or reached."""


class PageCreationError(OmniTestBrowserError):
    """Raised when a browser page cannot be created."""


class ContextCreationError(OmniTestBrowserError):
    """Raised when a browser context cannot be created."""
