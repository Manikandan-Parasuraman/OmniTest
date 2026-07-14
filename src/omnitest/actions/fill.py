"""Fill action helper."""

from .base import BaseAction


class FillAction(BaseAction):
    """Perform fill actions on input elements.

    The class is callable: calling it validates the selector and forwards
    the `value` to the Playwright `Locator.fill` API.
    """

    def __call__(
        self,
        selector: str,
        value: str,
        **kwargs,
    ):
        """Fill the element identified by `selector` with `value`.

        Extra keyword arguments are forwarded to Playwright's `fill`.
        """

        self.validate_selector(selector)

        locator = self.locator(selector)

        return self.execute(
            "fill",
            locator.fill,
            value,
            **kwargs,
        )
