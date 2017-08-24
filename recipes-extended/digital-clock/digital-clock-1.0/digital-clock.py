#!/usr/bin/env python

"""
main clock app
"""

import commands
import evdev
import subprocess
import os
from multiprocessing import Process

def digital_clock():

    # run qt digital clock
    retval = commands.getstatusoutput("/bin/qt-clock --platform eglfs")
    if retval[0] != 0:
        raise Exception("qt-clock error")

def ntp_query():

    # run ntpdate syncro
    while True:
        retval = commands.getstatusoutput("ntpdate 10.0.0.2")

def empty_evdev_fifo(result):

    # while there is data to process get all characters
    while result != None:
        # get the next data
        result = device.read_one()
    return 0

# set spaker to 100% volume
# configure WIFI IP
retval = commands.getstatusoutput("amixer set -D hw:0 'Headphone' 0dB")
if retval[0] != 0:
    raise Exception("amixer error")


# configure WIFI IP
retval = commands.getstatusoutput("ifconfig wlan0 10.0.0.1")
if retval[0] != 0:
    raise Exception("ifconfig error")

# prepare WIFI AP
fd = os.open("/tmp/foo.txt", os.O_RDWR|os.O_CREAT)
subprocess.Popen(["hostapd", "/etc/hostapdclock.conf"],
               stdin=None, stdout=fd, stderr=fd)

# configure Bluetooth
retval = commands.getstatusoutput("hciconfig hci0 up")
if retval[0] != 0:
    raise Exception("hciconfig hci0 up error")

retval = commands.getstatusoutput("hciconfig hci0 piscan")
if retval[0] != 0:
    raise Exception("hciconfig hci0 piscan error")

# initialize USB reader device
device = evdev.InputDevice('/dev/input/touchscreen0')

# run digital-clock qt display
p1 = Process(target=digital_clock)
p1.start()

# run ntp syncro
p2 = Process(target=ntp_query)
p2.start()

enablealarm = 0

# Infinite loop
while True:

    # scan bluetooth devices
    retval = commands.getstatusoutput("hcitool scan")
    if retval[0] != 0:
        raise Exception("hcitool scan")

    # search bluetooth id
    result = retval[1].find('88:79:7E:FC:B4:83')
    if result != -1:
        enablealarm = 1

    # there is data into evdev touchscrenn0?
    result = device.read_one()
    if result != None:
        empty_evdev_fifo(result)
        enablealarm = 0

    if  enablealarm:
        # enable alarm
        retval = commands.getstatusoutput("aplay /bin/alarm.wav")
        if retval[0] != 0:
            raise Exception("aplay error")

os.close(fd)
