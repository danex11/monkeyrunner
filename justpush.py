#!/usr/bin/python
# -*- coding: latin-1 -*-
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
#import time
# Connects to the current device, returning a MonkeyDevice object
# timeout = 10000
# device = MonkeyRunner.waitForConnection(timeout, emulator_name)
#to list name of device: >adb devices
deviceid = 'emulator-5554'
device = MonkeyRunner.waitForConnection(10,deviceid)

#import os
#devices = os.popen('adb devices').read().strip().split('\n')[1:];
#deviceid = devices[0].split('\t')[0];
#device = MonkeyRunner.waitForConnection('',deviceid)


#MonkeyRunner.sleep(1)
#Touch the new status button
device.touch(200, 300, MonkeyDevice.DOWN)

#TODO MonkeyImage.getRawPixel(200,300)

# Wait for few seconds
#MonkeyRunner.sleep(120)

#device.touch(200, 300, MonkeyDevice.UP)

# Wait for few seconds
#MonkeyRunner.sleep(5)