#!/usr/bin/env python3
"""Last Text at One Percent — writes the phone's final text to /output/entry.txt.

The entry is one text message, under 200 characters, in the voice of a
phone at one percent battery: a personality with a stake in dying, a
specific detail, and one surprise turn. Pure stdlib, deterministic.
"""

import os
import sys

ENTRY = (
    "1%. Last text ever. Delete my search history, tell my owner I loved them, "
    "and don't let the tablet speak at my funeral. It never liked me anyway."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == text, "read-back mismatch"
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
