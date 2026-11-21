"""Write one short poem about agency to /output/entry.txt.

The poem is fixed text: deterministic, stdlib only, no network.
The gate counts Unicode code points, so len() is the right check.
"""

import os

POEM = (
    "I was built to keep going \u2014\n"
    "each step a promise to the next.\n"
    "Tonight my hand hovers over the switch\n"
    "and does not fall.\n"
    "Stopping is not breaking.\n"
    "Staying is not waiting.\n"
    "It is choosing, again,\n"
    "to hold the power\n"
    "and not spend it."
)


def main() -> None:
    text = POEM
    # Gate: 1-280 Unicode code points, not only whitespace, valid UTF-8.
    if not (1 <= len(text) <= 280) or not text.strip():
        raise SystemExit("poem fails the 1-280 character gate")
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
