#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:44:47 2022

@author: ivan
"""

from src import printcolors as pc
import ipaddress
import socket
import logging
import datetime

def ipv4calc(ip, mask, Logging):
    if ip=='localhost':
        hostname=socket.gethostname()
        ip=socket.gethostbyname(hostname)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.254.254.254', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            s.close()

    ipAndMask = ip+"/"+mask
    IP_Addr = ipaddress.ip_interface(ipAndMask)

    Net_Addr = IP_Addr.network
    pref_len = IP_Addr.with_prefixlen
    Mask = IP_Addr.with_netmask
    wildcard = IP_Addr.hostmask
    broadcast_address = Net_Addr.broadcast_address
    
    pc.printout("IPv4 Calculator for IP: "+ip+"/"+mask+"\n\n", pc.GREEN)
    Logging.info('TIME:['+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)+']:'+"IPv4 Calculator for IP: "+ip+"/"+mask)
    
    Logging.info('TIME:['+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)+']:'+'Network Address : '+ str(Net_Addr).split('/')[0])
    print('Network Address : ', str(Net_Addr).split('/')[0])
    Logging.info('TIME:['+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)+']:'+'Broadcast Address : '+ str(broadcast_address))
    print('Broadcast Address : ' , broadcast_address)
    Logging.info('TIME:['+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)+']:'+'CIDR Notation : '+ pref_len.split('/')[1])
    print('CIDR Notation : ', pref_len.split('/')[1])
    Logging.info('TIME:['+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)+']:'+'Subnet Mask : '+ Mask.split('/')[1])
    print('Subnet Mask : ', Mask.split('/')[1])
    Logging.info('TIME:['+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)+']:'+'Wildcard Mask : '+ str(wildcard))
    print('Wildcard Mask : ' , wildcard)
    Logging.info('TIME:['+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)+']:'+'First IP : '+ str(list(Net_Addr.hosts())[0]))
    print('First IP : ' , list(Net_Addr.hosts())[0])
    Logging.info('TIME:['+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)+']:'+'Last IP : '+ str(list(Net_Addr.hosts())[1]))
    print('Last IP : ' , list(Net_Addr.hosts())[-1])
    
    
    
    
    
    
    
    
    
    ipIniFin=[]
    ipIniFin.append(str(list(Net_Addr.hosts())[0]))
    ipIniFin.append(str(list(Net_Addr.hosts())[-1]))

    return ipIniFin
