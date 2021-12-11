##!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import random


if __name__ == '__main__':
    # This is the Publisher
    wait_interval = 30

    while True:
        status = random.randint(0, 2)

        client = mqtt.Client()
        client.connect("192.168.1.59", 1883, 60)
        # client.publish("topic/test", "Hello world!")
        client.publish("traffic", status)
        client.disconnect()
        time.sleep(wait_interval)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
