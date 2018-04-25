#! /usr/bin/env python

import subprocess
import os

linia = '       K4'
tabCount = len(linia) - len(linia.lstrip('   '))
print(tabCount)

subprocess.call(['mkdir', 'K1'], shell= False)
subprocess.call(['mkdir', 'K1/K2'], shell= False)
subprocess.call(['mkdir', 'K1/K3'], shell= False)
subprocess.call(['mkdir', 'K1/K3/K4'], shell= False)
subprocess.call(['mkdir', 'K5'], shell= False)
subprocess.call(['mkdir', 'K5/K6'], shell= False)
