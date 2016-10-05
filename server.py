#!/usr/bin/python3

import socket

message = bytes("Hello Socket", "utf-8")

port = 8000#int(input("PORT? "))
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("127.0.0.1", port)) #socket.gethostname()
serversocket.listen(5)


(clientsocket, adress) = serversocket.accept()
serversocket.send(message)
serversocket.close()
