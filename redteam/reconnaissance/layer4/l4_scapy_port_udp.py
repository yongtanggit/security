#! /usr/bin/python3

## This program scans a range of UDP ports on a host with Python Scapy Module.
## It takes an IP address and an range of  UDP port numbers. 
## Found open port(s) will be printed to screen. 

import sys
import time
from scapy.all import *

def usage():
    print('USAGE: ', sys.argv[0], ' IP start-port-number end-port-number')

num=len(sys.argv)

if num == 4:
   ip=str(sys.argv[1])
   pst=int(sys.argv[2]) ## port range start
   ped=int(sys.argv[3]) + 1 ## port range end
else:
   usage()
   exit()

for p in range(pst,ped):
    a=sr1(IP(dst=ip)/UDP(dport=p),timeout=2,verbose=0)
    time.sleep(1)
    if a is None:
       print(p)
       

