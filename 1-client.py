#!/usr/bin/env python
import socket
import time

dip_addr = '127.0.0.1' 
DTCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockfd.connect((dip_addr, DTCP_PORT))

sockfd.send("Hello world".encode())

data = sockfd.recv(BUFFER_SIZE)

print(data)

time.sleep(1)

sockfd.close()
