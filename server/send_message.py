#!/usr/bin/python3

from socketIO_client import SocketIO

sio = SocketIO("localhost", 8080)

sio.emit("code", {"data": "6767"})
