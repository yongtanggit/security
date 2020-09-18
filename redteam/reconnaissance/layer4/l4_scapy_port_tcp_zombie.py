#!/usr/bin/python3

## This program performs idel scan(zombie scan). 
## It tests whether a host is a good zombie first before an indle scan.  

import time

import sys

from scapy.all import *


# Craft a packet probing zombie host. 
z_ip=str(input('IP of zombie host: '))
p_z=IP(dst=z_ip)/TCP(dport=80,flags='SA')

 
# This function identifys zombiehost. 
def check(tm):
   print('Testing the host.....')
   for i in range(tm):                 # More times of testing, more acurate the result is  
      res=sr1(p_z,timeout=2,verbose=0) # Send out the packet for response

      id_st=res[IP].id                 # First IPID

      res=sr1(p_z,timeout=2,verbose=0)

      id_end=res[IP].id                # Second IPID
    
      if id_end - id_st == 1:          # Calculate increment
          pass  
      else:
         print(z_ip, 'is not a good zombie.')
         sys.exit()
   print(z_ip, ' is a good zombie!')


# This function performs idle scan. 
def scan(): 
   t_ip=str(input('IP of target host: '))
   p_st=int(input('Port num starts: '))
   p_end=int(input('Port num ends: '))
   for i in range(p_st,p_end):
      res=sr1(p_z,timeout=2,verbose=0)                 # First probing
      id_st=res[IP].id
      p_t=IP(src=z_ip,dst=t_ip)/TCP(dport=i,flags='S') # Sproofing 
      send(p_t,verbose=0)
      res=sr1(p_z,timeout=2,verbose=0)                 # Second probing
      id_end=res[IP].id
      if id_end - id_st == 2:                          # Calculate increment
         print(i)

# Call the checker
check(10)

# Call the scanner 
#scan()




