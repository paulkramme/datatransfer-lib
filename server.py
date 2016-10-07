#!/usr/bin/env python3
import socket

TCP_IP = '' #FILL WITH IP WHICH REPRESENTS THE SERVER
TCP_PORT = 8000
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data:
		break
	print(str(data, 'utf-8'))
	#conn.send(data)
conn.close()

