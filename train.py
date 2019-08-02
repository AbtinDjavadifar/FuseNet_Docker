#!/usr/bin/env python

import subprocess

if __name__ == "__main__":
    
#    subprocess.check_call([
#      "bash", 
#      "./FuseNet_setup.sh"
#    ])
    
    subprocess.check_call([
      "docker",
      "build", ".",
      "-t", "segmentation:fusenet"
    ])
    subprocess.check_call([
    "docker",
    "run",
    "--rm",
    "--runtime=nvidia",
    "segmentation:fusenet",
    "train"
    ])