#!/usr/bin/env python3


import socket
import sys
import os
#from sendfile import sendfile


def transmit(path, TCP_IP, TCP_PORT = 8000):
	print(path)
	file = open(path, "r")
	blocksize = os.path.getsize(path)
	sock = socket.socket()
	sock.connect((TCP_IP, TCP_PORT))
	offset = 0
	while 1:
		sent = os.sendfile(sock.fileno(), file.fileno(), offset, blocksize)
		if sent == 0:
			print("Done.")
			break
		offset += sent


def receive(filename, TCP_PORT = 8000, TCP_IP = ''):
	#TCP_IP = '' #FILL WITH IP WHICH REPRESENTS THE SERVER
	file = open(filename, "wb")

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
	file.close()
	conn.close()


def main():
	if sys.argv[1] == "receive":
		receive(sys.argv[2])#, sys.argv[3], sys.argv[4])
	elif sys.argv[1] == "transmit":
		transmit(sys.argv[2], sys.argv[3])#, sys.argv[4])
	else:
		print("USAGE: " + sys.argv[0] + " transmit path ip port\nreceive path port ip")

if __name__ == __name__:
	main()
