"""Sample module proving the quality gate works before you replace src/."""

from __future__ import annotations


def build_greeting(name: str) -> str:
    """Return a friendly greeting for a non-empty name."""
    normalized_name = name.strip()
    if normalized_name == "":
        msg = "name must not be empty"
        raise ValueError(msg)
    return f"Hello, {normalized_name}!"
