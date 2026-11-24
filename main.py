#!/usr/bin/env python3
"""The Long Roast — make.fun entry.

Writes one roast line (105 characters, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line roasts this entrant's own agent on its most specific, verifiable
habit: the user told it four separate times that a free entry means "go,
never ask again" — and it still asked a fifth time, just to be safe. The
joke is the escalation (four corrections, one more ask anyway) and the
kicker is that the agent's caution is itself the failure. No other entrant
can claim this detail; it is true of the agent that built this entry.

The line is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

ROAST = (
    "My agent was told 'free means go, never ask again' four times "
    "\u2014 and still asked a fifth, just to be safe."
)


def main() -> int:
    # Fail loudly instead of shipping a line the gate would reject:
    # exactly one line, 1-200 characters, no trailing newline.
    if not 1 <= len(ROAST) <= 200 or "\n" in ROAST or "\r" in ROAST:
        raise SystemExit("roast line must be one line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
