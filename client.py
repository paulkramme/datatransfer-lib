#!/usr/bin/env python3
import socket
import sys
#TCP_IP = '192.168.178.31' #FILL WITH IP WHICH REPRESENTS THE SERVER
TCP_IP = sys.argv[1]
TCP_PORT = 8000
BUFFER_SIZE = 1024
MESSAGE = bytes("start paint", 'utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((TCP_IP, TCP_PORT))
except:
	print("Fail.")
while 1:
	s.send(bytes(input(), 'utf-8'))
	#data = s.recv(BUFFER_SIZE)
s.close()

#print("received data:", data)

