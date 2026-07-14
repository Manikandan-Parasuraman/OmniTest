"""Tests for the hello module."""

from omnitest import hello


def test_hello():
    """Verify the package greeting matches the expected string."""
    assert hello() == "Hello from OmniTest!"
