"""Type aliases and typing helpers for OmniTest.

This module centralizes project-specific typing helpers to keep other
modules' imports tidy.
"""

from typing import Any, Callable

# Example aliases (extend as needed)
JSONType = dict[str, Any]
Callback = Callable[..., Any]
