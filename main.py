"""One-line joke entry: the meeting that should have been an email."""

import os

LINE = "We spent an hour in the meeting that should have been an email, and the only thing we emailed afterwards was the invite to the next one."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
