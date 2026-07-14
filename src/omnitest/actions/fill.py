from .base import BaseAction


class FillAction(BaseAction):

    def __call__(
        self,
        selector: str,
        value: str,
        **kwargs,
    ):

        self.validate_selector(selector)

        locator = self.locator(selector)

        return self.execute(
            "fill",
            locator.fill,
            value,
            **kwargs,
        )
        