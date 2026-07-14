"""
Custom exceptions for the OmniTest Browser SDK.

The purpose of these exceptions is to provide framework-specific,
human-readable errors without exposing Playwright internals.
"""

from __future__ import annotations


class OmniTestError(Exception):
    """
    Base exception for all OmniTest errors.
    """

    default_message = "An unknown OmniTest error occurred."

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or self.default_message)


class BrowserError(OmniTestError):
    """
    Base exception for browser-related errors.
    """


class BrowserAlreadyStartedError(BrowserError):
    """
    Raised when attempting to start an already running browser.
    """

    default_message = "Browser has already been started."


class BrowserNotStartedError(BrowserError):
    """
    Raised when an operation requires an active browser.
    """

    default_message = "Browser has not been started."


class BrowserLaunchError(BrowserError):
    """
    Raised when the browser fails to launch.
    """

    default_message = "Unable to launch browser."


class BrowserClosedError(BrowserError):
    """
    Raised when attempting to interact with a closed browser.
    """

    default_message = "Browser session has already been closed."


class ContextCreationError(BrowserError):
    """
    Raised when a browser context cannot be created.
    """

    default_message = "Unable to create browser context."


class PageCreationError(BrowserError):
    """
    Raised when a page cannot be created.
    """

    default_message = "Unable to create browser page."


class NavigationError(BrowserError):
    """
    Raised when navigation to a URL fails.
    """

    default_message = "Failed to navigate to the requested URL."


class InvalidConfigurationError(BrowserError):
    """
    Raised when browser configuration is invalid.
    """

    default_message = "Invalid browser configuration."
