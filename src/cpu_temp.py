#!/usr/bin/env python

import os
import sys
import subprocess
import time

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


def get_cpu_temp():
    temp = float(subprocess.check_output(["cat", "/sys/devices/virtual/thermal/thermal_zone0/temp"])[:-2]
                 .decode("UTF-8"))/100
    return temp


if __name__ == "__main__":
    from pyA20.gpio import gpio
    from pyA20.gpio import port

    # Declare
    fan_pin = port.PA6

    # Init GPIO and declare outputs and inputs
    gpio.init()

    gpio.setcfg(fan_pin, gpio.OUTPUT)

    while 1:
        cpu_temp = get_cpu_temp()
        output = "CPU temp: {0}C".format(cpu_temp)
        print output
        if cpu_temp > 55:
            gpio.output(fan_pin, 1)
            time.sleep(5)
        else:
            gpio.output(fan_pin,0)
            time.sleep(5)
