from .parser import SelectorParser

class LocatorEngine:

    def __init__(self, page):
        self._page = page

    def find(self, selector):

        parsed = SelectorParser.parse(selector)

        strategy = parsed.strategy
        value = parsed.value

        handlers = {

            "css": lambda: self._page.locator(value),

            "xpath": lambda: self._page.locator(value),

            "text": lambda: self._page.get_by_text(value),

            "label": lambda: self._page.get_by_label(value),

            "placeholder": lambda: self._page.get_by_placeholder(value),

            "title": lambda: self._page.get_by_title(value),

            "alt": lambda: self._page.get_by_alt_text(value),

            "testid": lambda: self._page.get_by_test_id(value),

            "role": lambda: self._page.get_by_role(
                value[0],
                **value[1],
            ),
        }

        try:
            return handlers[strategy]()

        except KeyError:
            raise ValueError(
                f"Unsupported selector strategy '{strategy}'."
            )