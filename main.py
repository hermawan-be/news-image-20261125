"""Entry program for the make.fun news-image-20261125 bounty.

Copies the pre-built image entry.png shipped in this repository to
the output directory as entry.png.

The image sums up the world news of Wednesday 25 November 2026 in
one infographic: six stories from six regions and fields, with the
date named in the header.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        sys.stderr.write("entry.png not found next to main.py\n")
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)


if __name__ == "__main__":
    main()
