#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print 'mo-mama'
ww = s.recv(1024)
print ww
print "mo-mama\n\r"
vv = s.recv(1024)
print vv
print 'aft-yo mama!!\n\r'
s.close                     # Close the socket when done
