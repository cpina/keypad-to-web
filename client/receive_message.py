#!/usr/bin/env python3

from socketIO_client import SocketIO
import sys
from gpiozero import LED

ip = sys.argv[1]
led = LED(18)

def on_code(*args):
    global led
    message = args[0]
    print("on_code: ", message)

    if message == "6767":
        led.on()
    else:
        led.off()

sio = SocketIO(ip, 8080)

sio.on("news", on_code)
sio.wait()

