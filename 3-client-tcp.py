#!/usr/bin/env python

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("C. Creating socket success")

sockfd.connect((TCP_IP, TCP_PORT))
print ("C. Connect to server success")

i = 1

time.sleep(5)
while (i < 5):
	msg = (MESSAGE+ " " + str(i) + " Time").encode()
	print ("C. Sending message...")
	print ("\t\t", msg) 

	sockfd.send(msg)
	print ("C. Sending success...\n")

	data = sockfd.recv(BUFFER_SIZE)
	print ("C. Received message from server...")
	print ("\t\t", data)

	i += 1
	time.sleep(2)

sockfd.close()

print("received data:", data)
