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


def main() -> None:
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    try:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass
    print(ENTRY)


if __name__ == "__main__":
    main()
