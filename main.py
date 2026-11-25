#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

Gate: UTF-8 text, 1 to 200 characters, a single line, not whitespace only.
No network access, no dependencies beyond the standard library.
"""

import os

ENTRY = "My dog learned to sigh. Now every walk feels like a performance review."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate validation before writing: 1-200 chars, one line, not blank.
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry length {len(text)} outside 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be whitespace only")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read-back: verify exactly what was written before exiting.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        raise SystemExit("read-back mismatch: file content differs from entry")
    if not (1 <= len(written.rstrip("\n")) <= 200):
        raise SystemExit("read-back gate failed")


if __name__ == "__main__":
    main()
