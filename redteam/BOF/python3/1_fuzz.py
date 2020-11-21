#!/usr/bin/python3

### This program identifies BOF vulnerbility of email software.
### This program tests USER and PASS commands of POP3 by fuzzing.

import socket
import argparse


# Create chars to be send to buffer

def chars():
    buffer=['A']
    counter=100
    while len(buffer) <= 1000 :
        buffer.append('A'*counter)
        counter=counter+200
    return buffer

# Process options: -i(IP) -p(port) --user --pass
def option():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',help='IP adress')
    parser.add_argument('-p',help='Port number',type=int)
    parser.add_argument('--USER',help='USER command', action='store_true')
    parser.add_argument('--PASS',help='PASS command', action='store_true')
    args=parser.parse_args()
    return args


# Main

args=option()

buffer=chars()

for string in buffer:
     newline='\n'
     QUIT='QUIT\n'
     if args.USER:
        USER='USER '
        print('Fuzzing with USER ',len(string), ' byes.')
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connect = s.connect((args.i,110))
        s.recv(1024)
        s.send(USER.encode() + string.encode() + newline.encode())
        s.recv(1024)
        s.send(QUIT.encode())
        s.close
     if args.PASS:
        USER='USER TEST'
        PASS='PASS '
        print('Fuzzing with PASS ',len(string), ' byes.')
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connect = s.connect((args.i,110))
        s.recv(1024)
        s.send(USER.encode()+newline.encode())
        s.recv(1024)
        s.send(PASS.encode() + string.encode()+newline.encode())
        s.send(QUIT.encode())
        s.close
