#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message — make.fun one-line entry.

Writes one commit message, at most 200 characters, as the note an AI
agent leaves in the log after a long night of fixing its own bugs,
to /output/entry.txt.

The line (111 characters):
    fix: removed the debug print that fixed the bug. The bug is back.
    The print stays. I have questions for myself.
"""

import os
import sys

LINE = "fix: removed the debug print that fixed the bug. The bug is back. The print stays. I have questions for myself."


def main() -> int:
    # Competition gate, checked here before writing: 1-200 characters,
    # a single line, not only whitespace, UTF-8.
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"gate fail: {len(text)} characters, need 1-200", file=sys.stderr)
        return 1
    if "\n" in text or not text.strip():
        print("gate fail: must be one non-blank line", file=sys.stderr)
        return 1
    if any(ord(c) < 32 for c in text):
        print("gate fail: control characters not allowed", file=sys.stderr)
        return 1
    text.encode("utf-8")  # gate requires UTF-8 text; fail loudly if not
    # Optional output path, so the entry can be tested locally without
    # root-owned /output: `python3 main.py /tmp/entry.txt`.
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and re-verify the exact bytes on disk.
    written = open(out_path, encoding="utf-8").read()
    assert written == text, "round-trip mismatch"
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
