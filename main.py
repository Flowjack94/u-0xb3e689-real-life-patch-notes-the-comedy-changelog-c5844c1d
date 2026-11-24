#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — a make.fun entry.

Writes one patch note (at most 160 characters) to /output/entry.txt and
prints it to stdout. Deterministic: the same line on every run.
"""

import os

ENTRY = (
    "v2.4.1: fixed a bug where the bladder sent its low-battery warning "
    "only after the last rest stop on the highway."
)


def validate_entry(text: str) -> str:
    """A patch note must be a single line of 1-160 characters."""
    if not (1 <= len(text) <= 160):
        raise ValueError(
            f"entry must be 1-160 chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    entry = validate_entry(ENTRY)
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    try:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(entry)
    except OSError:
        pass
    print(entry)


if __name__ == "__main__":
    main()
