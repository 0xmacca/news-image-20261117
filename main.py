# news-image-20261117 entry (Python 3.13, standard library only).
#
# The entry image is the entry.png beside this file: a newspaper-style
# infographic summing up the world's news of Tuesday 17 November 2026
# (Kerch bridge hit, Hormuz tankers, Trump in Manila, JPMorgan outage,
# ULA Vulcan failure, plus three more stories in the bottom strip).
# The program copies those exact bytes to /output/entry.png, so two runs
# always write the same file. It uses no network and no third-party code.
#
# Run it outside the grader's container with:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import sys
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        print(f"error: source image not found: {src}", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size:
        print(
            f"error: output size mismatch: "
            f"{dst.stat().st_size} != {src.stat().st_size}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
