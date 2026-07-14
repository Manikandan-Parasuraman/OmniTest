"""Selector resolution engine."""

from collections.abc import Callable

from .parser import SelectorParser


class LocatorEngine:
    """Resolve normalized selectors into Playwright locators."""

    def __init__(self, page):
        """Initialize the locator engine."""
        self._page = page

    def find(self, selector):
        """Resolve a selector into a Playwright locator."""
        parsed = SelectorParser.parse(selector)

        handlers: dict[str, Callable] = {
            "css": self._find_css,
            "xpath": self._find_xpath,
            "text": self._find_text,
            "label": self._find_label,
            "placeholder": self._find_placeholder,
            "title": self._find_title,
            "alt": self._find_alt,
            "testid": self._find_testid,
            "role": self._find_role,
        }

        try:
            handler = handlers[parsed.strategy]
        except KeyError as exc:
            raise ValueError(f"Unsupported selector strategy '{parsed.strategy}'.") from exc

        return handler(parsed.value)

    def _find_css(self, value):
        """Resolve a CSS selector."""
        return self._page.locator(value)

    def _find_xpath(self, value):
        """Resolve an XPath selector."""
        return self._page.locator(value)

    def _find_text(self, value):
        """Resolve a text selector."""
        return self._page.get_by_text(value)

    def _find_label(self, value):
        """Resolve a label selector."""
        return self._page.get_by_label(value)

    def _find_placeholder(self, value):
        """Resolve a placeholder selector."""
        return self._page.get_by_placeholder(value)

    def _find_title(self, value):
        """Resolve a title selector."""
        return self._page.get_by_title(value)

    def _find_alt(self, value):
        """Resolve an alternative text selector."""
        return self._page.get_by_alt_text(value)

    def _find_testid(self, value):
        """Resolve a test ID selector."""
        return self._page.get_by_test_id(value)

    def _find_role(self, value):
        """Resolve an ARIA role selector."""
        return self._page.get_by_role(
            value[0],
            **value[1],
        )
