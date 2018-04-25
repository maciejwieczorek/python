#! /usr/bin/env python

import subprocess
import os

subprocess.call(["g++","test.cpp","-o","test.out"], shell = False)
with open(os.devnull, 'w') as devnull:
    exCode = subprocess.call(['.test.out'], stdout =devnull, shell =False)
    if (exCode == 0):
        print("OK")
    else:
        print("BLAD")

    
