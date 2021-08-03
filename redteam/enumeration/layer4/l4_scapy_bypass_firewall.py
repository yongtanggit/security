#! /usr/bin/python3

# This program detects firewall rules:
# 1) accpeted source ports
# 2) accepted source IP

from scapy.all import *


# target IP addres
dst_ip=input('IP: ')

###  Detect accepted source ports

# create a source ports range 
def source_port():
    start_port=input('Start Port Num: ')
    start_port=int(start_port)
    end_port=input('End port Num: ')
    end_port=int(end_port)

    print( 'Unfiltered Source Port:')

    for port in range(start_port, end_port):
        # send ACK with source ports
        t_response = sr1(IP(dst=dst_ip)/TCP(sport=port,flags='A'),timeout=1,verbose=0)
        # send UDP packet 
        u_response=sr1(IP(dst=dst_ip)/UDP(sport=port,dport=6000),timeout=1,verbose=0)
        # analyze the responds
        if t_response is not None:
            print('TCP: ', port)
        if u_response is not None:
            print('UDP: ', port)
        
### Detect accepted source IP
##  This part is incompleted. It requires other hacking methods such as ARP spoofing to work. 
def ip_addr():
    # Get network and host addresses. 
    prefix=input('Netowrk Address: ')
    start_host=input('Start Host: ')
    end_host=input('End Host: ')
    
    print('Unfiltered Source IP:')
    
    for host in range(int(start_host),int(end_host)):
        # send ACK with source IP
        host = str(host)
        src_ip=(prefix+'.'+host)
        ip_response = sr1(IP(src=src_ip,dst=dst_ip)/TCP(dport=6000,flags='S'),timeout=1,verbose=0)
        if ip_response is not None:
           print('IP: ', src_ip)
#ip_addr()
source_port()
