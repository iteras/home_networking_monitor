#!/usr/bin/env python
import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

# Declare ports
LED_green = port.PA12
LED_blue = port.PA11
LED_red = port.PA7

# Init GPIO and declare outputs and inputs
gpio.init()
gpio.setcfg(LED_red, gpio.OUTPUT)
gpio.setcfg(LED_green, gpio.OUTPUT)
gpio.setcfg(LED_blue, gpio.OUTPUT)

# Set all lights off
gpio.output(LED_red, 0)
gpio.output(LED_green, 0)
gpio.output(LED_blue, 0)

# Defining colors
all_colors = {LED_red, LED_green, LED_blue}
green = {LED_green}
red = {LED_red}
blue = {LED_blue}

yellow = {LED_green, LED_red }
magneta = {LED_blue, LED_red}
white = {LED_red, LED_blue, LED_green}


class LED_controller(object):

    class __LED_controller:
        def __init__(self):
            self.current_color = None
            self.running = None

        def __str__(self):
            return repr(self) + self.current_color

        def begin(self):
            self.running = True
            try:
                if self.current_color is not None:
                    print("COLOR CHANGED TO : %s" % self.current_color)
                    color = decide_color(self.current_color)
                    differences = list(set(all_colors) - set(color))
                    for led in color:
                        gpio.output(led, 1)
                    for led in differences:
                        gpio.output(led, x0)
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
