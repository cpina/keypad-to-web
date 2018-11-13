#!/usr/bin/env python3

from socketIO_client import SocketIO

sio = SocketIO("", 8080)

sio.emit("code", {"data": "6767"})
