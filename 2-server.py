#!/usr/bin/env python
import socket
import time

MY_IFACE = ''
TCP_PORT = 5005
BUFFER_SIZE = 20 

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockfd.bind((MY_IFACE, TCP_PORT))

sockfd.listen(5)

newfd, addr = sockfd.accept()
print('Connection address:', addr)

data = newfd.recv(BUFFER_SIZE)
print("received data:", data.decode())

newfd.send(data.upper())  # echo

newfd.close()
sockfd.close()

