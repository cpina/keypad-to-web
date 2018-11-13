#!/usr/bin/env python3

from socketIO_client import SocketIO
import sys

ip = sys.argv[1]
message = sys.argv[2]

sio = SocketIO(ip, 8080)

sio.emit("code", {"data": message})
