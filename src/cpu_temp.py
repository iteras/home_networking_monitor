#!/usr/bin/env python

import os
import sys
import subprocess
import time
import pycurl
import json

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


def get_cpu_temp():
    temp = float(subprocess.check_output(["cat", "/sys/devices/virtual/thermal/thermal_zone0/temp"])[:-2]
                 .decode("UTF-8"))/100
    return temp


def post_data(cpu_temp):
    c = pycurl.Curl()
    c.setopt(pycurl.URL, '192.168.0.100:8000/metrics/sbc_post')
    c.setopt(pycurl.HTTPHEADER, ['content-type: application/json'])
    data = json.dumps({"temperature" : cpu_temp, "ts" : time.time()})
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(pycurl.VERBOSE, 1)
    c.perform()
    print c.getinfo(pycurl.RESPONSE_CODE)
    #print(curl_agent.getinfo(pycurl.RESPONSE_CODE))
    c.close()

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
        try:
            post_data(cpu_temp)
        except:
            print("Could not communicate with server")
        print output
        if cpu_temp > 55:
            gpio.output(fan_pin, 1)
            time.sleep(5)
        else:
            gpio.output(fan_pin,0)
            time.sleep(5)
