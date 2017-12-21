#!/usr/bin/env python

import socket

#TCP_IP = '127.0.0.1'
TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 20 

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("S. Creating socket success")

sockfd.bind((TCP_IP, TCP_PORT))
print ("S. Binding on to port %d, Success" % (TCP_PORT))

sockfd.listen(5)

print ("S. Waiting for connection from clients...");

conn, addr = sockfd.accept()
print ("S. Got the connection request from ",  addr);

while 1:
	data = conn.recv(BUFFER_SIZE)
	print ("S. Received message from client...")
	print("\t\t", data)

	if not data: break

	print ("S. Seding reply to client as ...")
	data = data.upper()

	print ("S. Server response...")
	print ("\t\t", data)
	conn.send(data)  # echo

conn.close()
