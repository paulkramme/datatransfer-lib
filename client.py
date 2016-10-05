#!/usr/bin/env python3.5

import socket

ip = "127.0.0.1"#input("IP?")
port = 8000#int(input("Port?"))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
#s.recv = buffer
buffer = str(s.recv(1024), "utf-8")
#buffer.decode("utf-8")
print(buffer)
