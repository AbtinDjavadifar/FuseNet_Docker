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
            "fusenet_train.py",
            "--dataroot",
            "./datasets/nyu_class_10_db.h5",
            "--batch_size",
            "8",
            "--lr",
            "0.005"
        ],
            cwd=__location__
        )
