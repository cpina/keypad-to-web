#!/usr/bin/env python3

from socketIO_client import SocketIO

def on_code(*args):
    print("on_message", args)

sio = SocketIO("localhost", 8080)

sio.on("news", on_code)
sio.wait()

