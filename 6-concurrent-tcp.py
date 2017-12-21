#!/usr/bin/env python

import socket
import os
import time

#TCP_IP = '127.0.0.1'
TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 20 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("S. Creating socket success")

s.bind((TCP_IP, TCP_PORT))
print ("S. Binding on to port %d, Success" % (TCP_PORT))

s.listen(5)
print ("S. Waiting for connection from clients...");

tot_conn_count = 0
while(1):
	nfd, addr = s.accept()
	tot_conn_count += 1
	print ("\n\nS. Connection count ", tot_conn_count)
	print ("S. Got the connection request from ",  addr);
	if (os.fork() == 0):
		print('Connection address:', addr)
		while 1:
			data = nfd.recv(BUFFER_SIZE)
			print ("S. Received message from client...")
			print("\t\t", data)

			if not data: break

			print ("S. Seding reply to client as ...")
			data = data.upper()

			nfd.send(data)  # echo

		nfd.close()
		exit(1)
	else:
		nfd.close()

