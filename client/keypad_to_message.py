#!/usr/bin/env python3

from gpiozero import LED,PWMLED
from pad4pi import rpi_gpio
from signal import pause
import time
import sys
from socketIO_client import SocketIO

KEYPAD = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ["*",0,"#"]
]

stored_keys = []
# red = LED(1)
red = PWMLED(1)

ip = sys.argv[1]

#ROW_PINS = [23,24,25,8] # BCM numbering
#COL_PINS = [14,15,18,7] # BCM numbering

ROW_PINS = [24,23,18,15]
COL_PINS = [7,8,25]

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def send_keys(keys):
    message = "".join(keys)
    sio = SocketIO(ip, 8080)
    print("Should send:", message)
    sio.emit("code", {"data": message})

def storeKey(key):
    global stored_keys # yes, it's a hackday
    global red
    
    red.on()
    print("Pressed key:", key)
    if key == "#":
        send_keys(stored_keys)
    else:
        stored_keys.append(str(key))

    if len(stored_keys) > 4:
        stored_keys = stored_keys[1:]

    print("stored_key:", stored_keys)

keypad.registerKeyPressHandler(storeKey)

try:
    while True:
        time.sleep(0.5)
        red.off()

except KeyboardInterrupt:
    print("Goodbye!")

finally:
    keypad.cleanup()
