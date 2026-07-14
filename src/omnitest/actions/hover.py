from .base import BaseAction

class HoverAction(BaseAction):

    def __call__(self, selector: str, **kwargs):

        self.validate_selector(selector)

        locator = self.locator(selector)

        return self.execute(
            "hover",
            locator.hover,
            **kwargs,
        )