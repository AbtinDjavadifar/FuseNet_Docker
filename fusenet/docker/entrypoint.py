#!/usr/bin/env python

import sys
import subprocess
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

if __name__ == "__main__":
    cmd = sys.argv[1]

    if cmd == "train":
        # subprocess.check_call([
        #     "python",
        #     "process_nii.py"
        # ],
        #     cwd=__location__
        # )

        # subprocess.check_call([
        #     "python",
        #     "split_data.py"
        # ],
        #     cwd=__location__
        # )
        subprocess.check_call([
            "python",
            "masks2coco.py"
        ],
            cwd=__location__
        )
