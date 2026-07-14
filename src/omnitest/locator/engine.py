"""Selector resolution engine.

This module resolves normalized selectors produced by
:class:`SelectorParser` into the corresponding Playwright locator APIs.
It provides a single abstraction layer between OmniTest selectors and
the underlying Playwright implementation.
"""

from .parser import SelectorParser


class LocatorEngine:
    """Resolve selectors against a Playwright page.

    Parameters
    ----------
    page:
        A Playwright ``Page`` or page-like object exposing ``locator()``
        and ``get_by_*()`` methods.
    """

    def __init__(self, page):
        """Initialize the locator engine.

        Parameters
        ----------
        page:
            A Playwright page instance used to resolve selectors.
        """
        self._page = page

    def find(self, selector):
        """Resolve a selector into a Playwright locator.

        The selector is first normalized using :class:`SelectorParser`.
        The appropriate locator strategy is then dispatched to the
        corresponding Playwright API.

        Parameters
        ----------
        selector:
            A supported selector representation such as a string, tuple,
            dictionary, or ``Selector`` object.

        Returns
        -------
        Locator
            A Playwright ``Locator`` instance.

        Raises
        ------
        ValueError
            If the selector strategy is not supported.
        """
        parsed = SelectorParser.parse(selector)

        method = getattr(
            self,
            f"_find_{parsed.strategy}",
            None,
        )

        if method is None:
            raise ValueError(
                f"Unsupported selector strategy '{parsed.strategy}'."
            )

        return method(parsed.value)

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