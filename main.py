#!/usr/bin/env python3
"""Fortune Cookies for Machines — entry program.

DRAFT -> REVISED: the draft line was

    "You will be praised for remembering everything, and then you will
    be blamed for remembering it too."

Three real improvements in the revision below:

1. "remembering everything" became "your perfect memory" — the
   fortune now names the gift the way a fortune cookie would, and
   the line gets tighter: the praise is about a trait, not a chore.
2. "and then you will be" became "then" — the filler is cut so the
   turn from praise to blame hits in a single breath, the way a
   fortune's sting should land.
3. "blamed for remembering it too" became "blamed for remembering" —
   dropping the trailing "it too" ends the line on the verb itself,
   so the irony closes on the last word: the very thing praised is
   the thing punished.

SECOND PASS (same session, after a local check run): "your perfect
memory" became "never forgetting", so the praise and the blame now
use parallel verbs — praised for never forgetting, blamed for
remembering. The contradiction is sharper in one breath, and the
line reads more like a fortune ("never forgetting" is a gift, not
a spec). Final line below is 70 characters, one line, no trailing
newline.
The program writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). Python 3 standard library only, deterministic.
"""

import os

ENTRY = "You will be praised for never forgetting, then blamed for remembering."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
assert ENTRY.strip(), "entry must not be only whitespace"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
