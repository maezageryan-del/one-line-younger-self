#!/usr/bin/env python3
"""One line to your younger self, for make.fun.

Writes the single line the older self would send back to the younger self
to the harness output file. The text is fixed: one sentence, one line, no
trailing newline, 153 characters.
"""

import os

ENTRY = (
    "The friend you lose over a borrowed bike is the one you'll still "
    "look for in every crowd at forty \u2014 ride back now, kid, and "
    "return it before summer ends."
)


def main() -> None:
    # The sealed gate accepts 1-200 characters, non-blank, one line.
    # Fail loudly here rather than shipping a file the gate would refuse.
    # The em-dash is a single character (U+2014); the count is in characters,
    # not bytes, so 153 chars / 155 bytes both sit inside the gate.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() and "\n" not in ENTRY
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
