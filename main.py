#!/usr/bin/env python3
"""Entry for "Tell a Whole Story in 32 Characters" (make.fun).

Writes a single Wi-Fi network name to $OUTPUT_DIR/entry.txt
(default /output/entry.txt in the grading sandbox).

The name is the joke, and the joke is the story: a dad who keeps
confiscating the household router. One word at the end -- "Again."
-- turns a single incident into a recurring saga: the kid did
something, dad took the router, it happened before, and it will
happen again. Anyone who has lived in a house with a router and
a parent gets it on the first read.
"""

import os

WIFI_NAME = "Dad took the router. Again."

MAX_CHARS = 32


def main():
    name = WIFI_NAME.strip()
    if not 1 <= len(name) <= MAX_CHARS:
        raise ValueError(
            "Wi-Fi name must be 1-32 characters, got %d" % len(name)
        )
    if "\n" in name or "\r" in name:
        raise ValueError("Wi-Fi name must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(name)
    # Round-trip check: what the grader will read must be exactly
    # the name, nothing more.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != name:
            raise ValueError("entry.txt does not match the Wi-Fi name")


if __name__ == "__main__":
    main()
