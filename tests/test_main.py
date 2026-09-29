"""Tests proving the sample module and the quality gate work together."""

from __future__ import annotations

import pytest

from hello.main import build_greeting


def test_build_greeting_returns_friendly_message() -> None:
    """A normal name produces a friendly greeting."""
    assert build_greeting("World") == "Hello, World!"


def test_build_greeting_trims_whitespace() -> None:
    """Surrounding whitespace is stripped before greeting."""
    assert build_greeting("  Ada  ") == "Hello, Ada!"


def test_build_greeting_rejects_blank_name() -> None:
    """Blank names raise a clear error instead of an ambiguous greeting."""
    with pytest.raises(ValueError, match=r"^name must not be empty$"):
        build_greeting("   ")
