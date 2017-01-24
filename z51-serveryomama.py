#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   ww =   str(('...connection fm - ', addr))
   vv = '\n\r   ...+ thanks for shopping our kmart!!'
   print 'sending - ', ww
   c.send(ww)
   print 'yo-mama!!'
   print 'sending - ', vv
   c.send(vv)
   c.close()                # Close the connection
