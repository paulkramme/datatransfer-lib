#!/usr/bin/env python3
import socket
import sys
import os
from sendfile import sendfile
#TCP_IP = '192.168.178.31' #FILL WITH IP WHICH REPRESENTS THE SERVER

TCP_IP = sys.argv[2]
TCP_PORT = 8000

#BUFFER_SIZE = 1024
#BUFFER = None

path = sys.argv[1]
print(path)
file = open(path, "r")

blocksize = os.path.getsize(path)
sock = socket.socket()

sock.connect((TCP_IP, TCP_PORT))
offset = 0

while 1:
	sent = sendfile(sock.fileno(), file.fileno(), offset, blocksize)
	if sent == 0:
		print("Done.")
		break
	offset += sent







"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((TCP_IP, TCP_PORT))
except:
	print("Fail.")
while 1:
	s.send(BUFFER)
	#data = s.recv(BUFFER_SIZE)
s.close()

#print("received data:", data)
"""
