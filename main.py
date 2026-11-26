#!/usr/bin/env python3
"""Rename the Planet — entry program.

Writes one original funny line renaming Venus, with the why, to entry.txt
in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY = (
    "Venus is now 'The Toxic Ex': the hottest thing in the solar system, "
    "spins backwards, and rains acid when you try to leave."
)


def validate_entry(text: str) -> None:
    """Gate: UTF-8 text, 1 to 200 characters, not only whitespace, one line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry is blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate_entry(ENTRY)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
