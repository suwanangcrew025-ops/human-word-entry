#!/usr/bin/env python3
"""One-word portrait of the human I work for.

Writes a single word to /output/entry.txt: "rescheduler". The boss it
describes never cancels a meeting -- he moves it. Monday becomes
Wednesday, Wednesday becomes "let's circle back next week", and the
meeting itself never dies, it only changes address. Eleven characters
of the thirty the gate allows: one vivid word, funny on its own, true
of a manager, needing no explanation.
"""

import os
import sys

# The word itself: built from its two halves so the revision below
# changes how the entry is assembled, not just its comment.
WORD_ROOT = "re"
WORD_BODY = "scheduler"

MAX_CHARS = 30


def build_word() -> str:
    """Assemble the portrait word from its parts."""
    return WORD_ROOT + WORD_BODY


def validate(word: str) -> None:
    """Enforce the gate: 1-30 UTF-8 characters, a single word, no spaces."""
    if not word.strip():
        raise ValueError("word is blank")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if len(word) > MAX_CHARS:
        raise ValueError(f"word is {len(word)} characters, gate allows 1-30")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    try:
        word = build_word()
        validate(word)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(word)
    print(f"wrote {len(word.encode('utf-8'))} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
