#!/usr/bin/env python

import os
import sys
import subprocess

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

def get_cpu_temp():
    temp = float(subprocess.check_output(["cat", "/sys/devices/virtual/thermal/thermal_zone0/temp"])[:-2]
                 .decode("UTF-8"))/100
    return temp