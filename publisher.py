#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import sys


print ("argv[0]: %s" % (sys.argv[1]))

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("test", argv[1]);