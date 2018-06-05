#!/usr/bin/python3

import subprocess
import sys
import json
sys.path.insert(0,'/home/pi/SmartHome/src/')
import led_controller

WARNING = 70
BAD = 200


def ping():
    try:
        return subprocess.check_output(["ping -I wlan0 -c 4 www.google.com"], shell=True).decode("UTF-8").split("\n")
    except subprocess.CalledProcessError:
        return None

def get_data(ping):
    data = {}
    loss_data_raw = ping[-3] # Get data row for losses
    ping_data_raw = ping[-2] # Get data row for response times

    # Find losses
    tmp = loss_data_raw.split(',')
    ping_packets_sent = float(tmp[0].split(" ")[0])
    ping_packets_received = float(tmp[1].split(" ")[1])
    loss = ping_packets_sent - ping_packets_received

    # Find ping response times(avg, min, max, mdev)
    tmp = ping_data_raw.split('=')
    ping_data_tag = tmp[0].strip().split(" ")[1].split("/")
    ping_data_values = tmp[1].strip().split(" ")[0].split("/")
    for i in range(len(ping_data_tag)):
        data[ping_data_tag[i]] = float(ping_data_values[i])
    data["losses"] = loss
    return data


def decide_status(data):
    if float(data["avg"]) >= BAD:
        return "red"
    elif float(data["avg"]) >= WARNING:
        return "yellow"
    elif float(data["avg"]) < WARNING:
        return "green"


if __name__ == "__main__":
    controller = None
    result = None
    try:
        while True:
            ping_result = ping()
            if ping_result is not None:
                data = get_data(ping_result)
                print(data["avg"])
                result = decide_status(data)
                print(result)
            else:
                print(ping_result)
                result = "magneta"
            if controller is None:
                controller = led_controller.LED_controller()
            controller.current_color = result
            controller.begin()

    except KeyboardInterrupt:
        print("Goodbye.")

    #TODO: give out appropriate command to MC