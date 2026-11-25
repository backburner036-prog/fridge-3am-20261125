"""Fridge-text entry for make.fun: one line, at most 140 chars.

The program writes LINE verbatim to /output/entry.txt (109 chars).
"""

from pathlib import Path

LINE = "3am. I counted your leftovers again. There are four. You will eat one, feel guilty about three, and blame me."
ENTRY_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the entry text, creating /output when needed."""
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
