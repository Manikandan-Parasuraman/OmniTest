"""Browser configuration models for OmniTest."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

from omnitest.core.constants import (
    DEFAULT_BROWSER,
    DEFAULT_COLOR_SCHEME,
    DEFAULT_TIMEOUT,
)

BrowserType = Literal["chromium", "firefox", "webkit"]
ColorScheme = Literal["light", "dark", "no-preference"]


@dataclass(slots=True)
class BrowserConfig:  # pylint: disable=too-many-instance-attributes
    """Configuration options for launching and configuring a browser."""

    browser: BrowserType = DEFAULT_BROWSER
    headless: bool = True
    channel: str | None = None
    slow_mo: int = 0

    viewport: tuple[int, int] = (1920, 1080)
    locale: str = "en-US"
    timezone: str = "UTC"
    base_url: str | None = None
    user_agent: str | None = None
    accept_downloads: bool = True
    downloads_path: Path | None = None
    ignore_https_errors: bool = False
    java_script_enabled: bool = True
    color_scheme: ColorScheme = DEFAULT_COLOR_SCHEME
    permissions: list[str] = field(default_factory=list)
    extra_http_headers: dict[str, str] = field(default_factory=dict)
    storage_state: str | Path | None = None

    record_video: bool = False
    video_dir: Path | None = None
    tracing: bool = False

    timeout: float = DEFAULT_TIMEOUT
    navigation_timeout: float = DEFAULT_TIMEOUT

    proxy: dict[str, Any] | None = None
    http_credentials: dict[str, str] | None = None
    offline: bool = False

    geolocation: dict[str, float] | None = None
    device_scale_factor: float = 1.0
    is_mobile: bool = False
    has_touch: bool = False

    def __post_init__(self) -> None:
        """Validate configuration values."""
        if self.viewport[0] <= 0:
            raise ValueError("Viewport width must be greater than zero.")

        if self.viewport[1] <= 0:
            raise ValueError("Viewport height must be greater than zero.")

        if self.timeout < 0:
            raise ValueError("Timeout cannot be negative.")

        if self.navigation_timeout < 0:
            raise ValueError("Navigation timeout cannot be negative.")

        if self.slow_mo < 0:
            raise ValueError("slow_mo cannot be negative.")

    @property
    def launch_options(self) -> dict[str, Any]:
        """Convert configuration into Playwright browser launch options."""
        options: dict[str, Any] = {
            "headless": self.headless,
            "slow_mo": self.slow_mo,
            "proxy": self.proxy,
        }

        if self.channel:
            options["channel"] = self.channel

        return options

    @property
    def context_options(self) -> dict[str, Any]:
        """Convert configuration into Playwright browser context options."""
        options: dict[str, Any] = {
            "viewport": {
                "width": self.viewport[0],
                "height": self.viewport[1],
            },
            "locale": self.locale,
            "timezone_id": self.timezone,
            "accept_downloads": self.accept_downloads,
            "ignore_https_errors": self.ignore_https_errors,
            "java_script_enabled": self.java_script_enabled,
            "color_scheme": self.color_scheme,
            "permissions": self.permissions,
            "extra_http_headers": self.extra_http_headers,
            "offline": self.offline,
            "is_mobile": self.is_mobile,
            "has_touch": self.has_touch,
            "device_scale_factor": self.device_scale_factor,
        }

        if self.user_agent:
            options["user_agent"] = self.user_agent

        if self.base_url:
            options["base_url"] = self.base_url

        if self.storage_state:
            options["storage_state"] = str(self.storage_state)

        if self.http_credentials:
            options["http_credentials"] = self.http_credentials

        if self.geolocation:
            options["geolocation"] = self.geolocation

        if self.record_video:
            options["record_video_dir"] = str(self.video_dir or Path("videos"))

        return options
