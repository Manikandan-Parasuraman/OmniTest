"""Click action helper."""

from .base import BaseAction


class ClickAction(BaseAction):
    """Perform click actions on elements matched by a selector.

    This callable class validates the selector, resolves a locator and
    executes the Playwright `click` operation with shared action hooks.
    """

    def __call__(self, selector: str, **kwargs):

        """Click the element identified by `selector`.

        Any additional keyword arguments are forwarded to Playwright's
        `Locator.click` implementation.
        """

        self.validate_selector(selector)

        locator = self.locator(selector)

        return self.execute(
            "click",
            locator.click,
            **kwargs,
        )