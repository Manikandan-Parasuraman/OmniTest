"""Hover action helper."""

from .base import BaseAction


class HoverAction(BaseAction):
    """Perform hover actions over elements.

    Validates the selector, resolves the locator, and calls Playwright's
    `hover` with shared action lifecycle hooks.
    """

    def __call__(self, selector: str, **kwargs):

        """Hover over the element identified by `selector`."""

        self.validate_selector(selector)

        locator = self.locator(selector)

        return self.execute(
            "hover",
            locator.hover,
            **kwargs,
        )
