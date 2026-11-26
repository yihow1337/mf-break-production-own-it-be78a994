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
OUTPUT_NAME = "entry.txt"

# The gate accepts UTF-8 text of 1 to 200 characters that is not only
# whitespace. We mirror those bounds here so a bad edit to entry.txt fails
# loudly during our own run rather than silently at the gate.
MIN_CHARS = 1
MAX_CHARS = 200


def load_line(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    # One line only: no stray newlines, no leading or trailing whitespace.
    return " ".join(text.split())


def validate(line):
    # Return the line unchanged if it clears the gate, else exit with a reason.
    if len(line) < MIN_CHARS:
        sys.exit("entry.txt is empty or only whitespace")
    if len(line) > MAX_CHARS:
        sys.exit("entry is %d characters, over the %d limit" % (len(line), MAX_CHARS))
    return line


def write_artifact(line):
    # Write the line as exact UTF-8 bytes, no trailing newline, so every run
    # produces byte-identical output. Create the output dir if it is missing.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_NAME)

    with open(out_path, "wb") as handle:
        handle.write(line.encode("utf-8"))
    return out_path


def main():
    line = validate(load_line(SOURCE))
    out_path = write_artifact(line)
    print("wrote %s (%d characters)" % (out_path, len(line)))


if __name__ == "__main__":
    main()
