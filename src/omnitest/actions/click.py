from .base import BaseAction


class ClickAction(BaseAction):

    def __call__(self, selector: str, **kwargs):

        self.validate_selector(selector)

        locator = self.locator(selector)

        return self.execute(
            "click",
            locator.click,
            **kwargs,
        )