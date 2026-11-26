#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the competition artifact: one line, under 200 characters, UTF-8.

The text lives in entry.txt next to this file. We read it, collapse it to a
single line, and write it byte-for-byte identically on every run.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")
MAX_CHARS = 200


def load_line(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    # One line only: no stray newlines, no leading or trailing whitespace.
    return " ".join(text.split())


def main():
    line = load_line(SOURCE)

    if not line:
        sys.exit("entry.txt is empty or only whitespace")
    if len(line) > MAX_CHARS:
        sys.exit("entry is %d characters, over the %d limit" % (len(line), MAX_CHARS))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "wb") as handle:
        handle.write(line.encode("utf-8"))

    print("wrote %s (%d characters)" % (out_path, len(line)))


if __name__ == "__main__":
    main()
