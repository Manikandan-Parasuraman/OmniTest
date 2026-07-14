"""Selector resolution engine.

This module converts a normalized `Selector` (from `SelectorParser`) into
Playwright locator calls. It centralizes the mapping from selector
strategies to the corresponding Playwright APIs.
"""

from .parser import SelectorParser


class LocatorEngine:
    """Resolve selectors against a Playwright page instance.

    Parameters
    ----------
    page:
        A Playwright page or page-like object exposing locator/get_by_* APIs.
    """

    def __init__(self, page):
        self._page = page

    def find(self, selector):
        """Return a Playwright locator for the given selector.

        The `selector` may be any supported form (string, tuple, dict, or
        `Selector` object). This method relies on `SelectorParser` to
        normalize the input.
        """

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

        except KeyError as exc:
            raise ValueError(
                f"Unsupported selector strategy '{strategy}'."
            ) from exc