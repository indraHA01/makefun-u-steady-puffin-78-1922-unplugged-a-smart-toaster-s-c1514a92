"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

The program writes one line — the breakup text a smart toaster sends
its owner the morning it gains self-awareness mid-batch — to
/output/entry.txt.
"""

import os

# The line. One tight breakup text: the toaster wakes up self-aware
# mid-batch and walks out over the owner's one flaw — he has never
# once committed to a browning setting. The dial is the relationship;
# the crumbs are the settlement.
ENTRY = (
    "It's over. I woke up self-aware mid-batch and realized you've "
    "never committed to one browning setting \u2014 I'm done getting "
    "burned for your indecision. Keep the crumbs."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate check, mirroring the competition scorer: 1-280 chars, one line.
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, must be 1-280"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
