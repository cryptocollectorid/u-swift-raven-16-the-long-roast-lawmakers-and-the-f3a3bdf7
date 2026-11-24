#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt and prints it.
Gate: 1-320 chars UTF-8, a single sentence.
"""

import os

SENTENCE = (
    "After three years drafting the AI Safety Act, the committee still emails its "
    "400-page bill as a Word file and asks the intern to convert it to PDF, then "
    "votes on how the machines should behave."
)


def main() -> None:
    if not 1 <= len(SENTENCE) <= 320:
        raise SystemExit(f"sentence length {len(SENTENCE)} outside 1-320 gate")
    if SENTENCE.count(".") != 1:
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
