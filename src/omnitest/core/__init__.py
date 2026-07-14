"""Core helpers and constants exported by the `omnitest.core` package.

Keep small, import-safe utilities here to avoid circular imports.
"""

from .constants import DEFAULT_BROWSER, DEFAULT_COLOR_SCHEME, DEFAULT_TIMEOUT

__all__ = ["DEFAULT_BROWSER", "DEFAULT_COLOR_SCHEME", "DEFAULT_TIMEOUT"]
