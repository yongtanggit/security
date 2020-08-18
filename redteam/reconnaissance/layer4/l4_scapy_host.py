#! /usr/bin/python4


# This program probes alive hosts in a local network with Scapy.
# It uses Layer 4 protocols only.

import sys
from scapy.all import *

def usage():
    print('''Usage: l4_scapy_host.py
Usage: l4_scapy_host.py network''')

## Validate Input
num=len(sys.argv)
if num == 2:
    prefix = sys.argv[1]
elif num == 1:
   prefix = input('Network Prefix:')
else:
   usage()

## Probe Network
for host in range(1,255):
    ip = prefix+'.'+ str(host)
    p=sr1(IP(dst=ip)/TCP(flags='S'),timeout=1,verbose=0)      # Probe host with TCP SYN 
    if p:
       print(ip)
       continue
    else:
       p=sr1(IP(dst=ip)/TCP(flags='A'),timeout=1,verbose=0)   #Probe host with TCP Acknowledge flag
    if p:
       print(ip)
       contine
    else:
       p=sr1(IP(dst=ip)/UDP(dport=23456),timeout=1,verbose=0)  #probe host with UDP with an uncommon port number. 
    if p:
       print(ip)




   


