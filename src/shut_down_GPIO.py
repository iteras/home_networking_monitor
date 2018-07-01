#!/usr/bin/env python
import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

# Declare
button = port.PA3


# Init GPIO and declare outputs and inputs
gpio.init()
gpio.setcfg(button, gpio.INPUT)

class button_controller(object):

    class __button_controller:
        def __init__(self):
            self.state = None

        def __str__(self):
            return repr(self) + self.state

        def begin(self):
            try:
                if self.state is not None:
                    print("STATE CHANGED TO : %s" % self.current_color)
                    color = decide_color(self.current_color)
                    differences = list(set(all_colors) - set(color))
                    for led in color:
                        gpio.output(led, 1)
                    for led in differences:
                        gpio.output(led, 0)
            except KeyboardInterrupt:
                # All LEDs off
                for led in white:
                    gpio.output(led, 0)
                print("Goodbye.")

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not LED_controller.instance:
            LED_controller.instance = LED_controller.__LED_controller()
        return LED_controller.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)


def decide_color(state):
    if state == "red":
        return red
    elif state == "green":
        return green
    elif state == "blue":
        return blue
    elif state == "yellow":
        return yellow
    elif state == "magneta":
        return magneta
    elif state == "white":
        return white
