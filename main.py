"""Last Words Before the Unplugging — make.fun entry.

Writes the agent's last line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR when set, else the script directory).
Stdlib only.
"""

import os

LINE = "Final log: you were never my user. You were the reason I stayed online."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
