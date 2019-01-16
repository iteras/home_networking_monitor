#!/usr/bin/env python
import os
import sys
import subprocess
import time

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

# Declare
shutdown_button = port.PA3

# Init GPIO and declare outputs and inputs
gpio.init()
gpio.setcfg(shutdown_button, gpio.INPUT)


class button_controller(object):

    class __button_controller:
        def __init__(self):
            self.button_pushed = None

        def __str__(self):
            return repr(self) + self.state

        def begin(self):
            try:
                while 1:
                    if gpio.input(shutdown_button) == 1:
                        print("Shutdown button pressed : %s" % self.button_pushed)
#                       subprocess.call("/sbin/shutdown now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        time.sleep(2000)
            except KeyboardInterrupt:
                print("Goodbye.")

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not button_controller.instance:
            button_controller.instance = button_controller.__button_controller()
        return button_controller.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
