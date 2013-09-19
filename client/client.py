#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345
                # Reserve a port for your service.

s.connect((host, port))
BUFFER_SIZE = 8
while True:

	print "connected"
	#for i in range(BUFFER_SIZE):
		#size = s.recv(1024)
		#print size
		#changed_s = s.recv(1024)
		#if changed_s == "" or changed_s == '\0':
	#		break
	#	print changed_s
s.close 