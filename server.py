#!/usr/bin/env python3
import socket

TCP_IP = '' #FILL WITH IP WHICH REPRESENTS THE SERVER
TCP_PORT = 8000
#BUFFER_SIZE = 1024

file = open("yay", "wb")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
	data = conn.recv(4096)
	if not data:
		print("Done")
		break
	file.write(data)
	#conn.send(data)
file.close()
conn.close()

