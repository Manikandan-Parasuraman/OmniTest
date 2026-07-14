"""Top-level package for omnitest."""

from . import actions, browser, exceptions, logger


def hello() -> str:
    """Return the package greeting."""
    return "Hello from OmniTest!"


__all__ = ["actions", "browser", "exceptions", "logger", "hello"]
