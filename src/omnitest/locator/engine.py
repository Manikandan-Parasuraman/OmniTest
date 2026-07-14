from collections.abc import Callable

from .parser import SelectorParser


class LocatorEngine:
    ...

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
            raise ValueError(
                f"Unsupported selector strategy '{parsed.strategy}'."
            ) from exc

        return handler(parsed.value)