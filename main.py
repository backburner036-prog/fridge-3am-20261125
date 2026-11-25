"""One line: a text from the fridge at 3am.

Writes a single line (109 chars, cap 140) to /output/entry.txt.
"""

from pathlib import Path

LINE = "3am. I counted your leftovers again. There are four. You will eat one, feel guilty about three, and blame me."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
