#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep
has been fixed, to /output/entry.txt.
"""

import os

LINE = "Fixed: humans can now fall asleep without first replaying every embarrassing moment since 2009."


def main() -> None:
    # Gate: entry must be 1-160 characters, not only whitespace.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
