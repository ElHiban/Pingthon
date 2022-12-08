#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:44:47 2022

@author: ivan
"""

from methods import ipv4calculator
from methods import progressBar as pb
from src import printcolors as pc
import socket
import sys
import os
import datetime
import logging

#scanner code
def netScan(ip_addr, port, verbose):
    #ip_addr = 'localhost'
    #portList = [21,22,23,80]
    portList = [port]
    print("Doing ping to the IP: "+ip_addr+"\n")
    
    for port in portList:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            status = sock.connect_ex((ip_addr, port))
            if status == 0:
                print(f"Port: {port} - OPEN")
            else:
                print(f"Port: {port} - CLOSED")
            sock.close()
        except socket.error as err:
            print(f"Connection error: {err}")    
            sys.exit()

#Scan all the ports for multiples IPs for a given mask
def IPSwMask4Port(ip, mask, port, log, logOutput, dir_addr, verbose):
    
    if log==True:
        if logOutput==None:
            if not os.path.exists(dir_addr+"/logs"):
                os.makedirs(dir_addr+"/logs")
            now = datetime.datetime.now()
            logging.basicConfig(filename=dir_addr+"/logs/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG)
        else:
           if not os.path.exists(logOutput):
                os.makedirs(logOutput)
           now = datetime.datetime.now()
           logging.basicConfig(filename=logOutput+"/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG)
    
    ipIniFin = ipv4calculator.ipv4calc(ip, mask, logging)
    
    print("\nThe ping will be done for the given ports, for the IP range from "+ipIniFin[0]+" to the IP "+ipIniFin[1]+" both included\n")
    
    #CALCULAR LA IP INI HASTA LA FINAL EJEMPLO (1 A 254 = 254 ips eso por la cantidad de puertos para sabes el porcentaje que hay que asignar a la progressbar
    
    lenPb=0
    
    if mask=='8':
       print("The mask 8 has been selected")
       print("Sorry for the inconvenince. This feature is currently not working")
       sys.exit() 
      
    if mask=='16':
       print("The mask 16 has been selected")
       print("Sorry for the inconvenince. This feature is currently not working")
       sys.exit()  
    
    if mask=='24':
        lenPb = 254
        ipIniL = ipIniFin[0].split(".")
        ipMaxL = ipIniFin[1].split(".")
    
        ipIni = int(ipIniL[3])
        ipMax = int(ipMaxL[3])
        
        ip_addrB = ipIniL[0]+"."+ipIniL[1]+"."+ipIniL[2]+"."
    
    if mask=='32':
       print("The mask 32 has been selected")
       print("Sorry for the inconvenince. This feature is currently not working")
       sys.exit()
       
    openPorts = []
    closedPorts = []
    
    pb.printProgressBar(0, lenPb, prefix = 'Progress:', suffix = 'Complete', length = 60)
    
    while ipIni < ipMax:
        try:
            ip_addr = ip_addrB+str(ipIni)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            status = sock.connect_ex((ip_addr, int(port)))
            if status == 0:
                if verbose:
                    print("IP: "+ip_addr+"                                                                                          ",end="\r\n")
                    print(f"Port: {port} - OPEN                                                                                       ", end="\r\n")
                openPorts.append(port)
            else:
                if verbose:
                    print("IP: "+ip_addr+"                                                                                          ",end="\r\n")
                    print(f"Port: {port} - CLOSED                                                                                       ", end="\r\n") #The free space is necesary in order to delete the previous output that was the progress bar
                closedPorts.append(port)
            sock.close()
            ipIni += 1
            # Update Progress Bar
            pb.printProgressBar(int(ipIni), lenPb, prefix = 'Progress:', suffix = 'Complete', length = 60)
        except socket.error as err:
            print(f"Connection error: {err}")    
            sys.exit()
    print(f"\nOpen ports: {openPorts}")

#Scan all the ports for multiples IPs for a given mask
def IPSwMask4Ports(ip, mask, ports, log, logOutput, dir_addr, verbose):
    
    if log==True:
        if logOutput==None:
            if not os.path.exists(dir_addr+"/logs"):
                os.makedirs(dir_addr+"/logs")
            now = datetime.datetime.now()
            logging.basicConfig(filename=dir_addr+"/logs/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG)
        else:
           if not os.path.exists(logOutput):
                os.makedirs(logOutput)
           now = datetime.datetime.now()
           logging.basicConfig(filename=logOutput+"/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG) 
    
    ipIniFin = ipv4calculator.ipv4calc(ip, mask, logging)
    
    print("\nThe ping will be done for the given ports, for the IP range from "+ipIniFin[0]+" to the IP "+ipIniFin[1]+" both included\n")
    #f.write("\nThe ping will be done for the given ports, for the IP range from "+ipIniFin[0]+" to the IP "+ipIniFin[1]+" both included\n")
    
    #CALCULAR LA IP INI HASTA LA FINAL EJEMPLO (1 A 254 = 254 ips eso por la cantidad de puertos para sabes el porcentaje que hay que asignar a la progressbar
    
    lenPb=0
    
    if mask=='8':
       print("The mask 8 has been selected")
       print("Sorry for the inconvenince. This feature is currently not working")
       sys.exit() 
      
    if mask=='16':
       print("The mask 16 has been selected")
       print("Sorry for the inconvenince. This feature is currently not working")
       sys.exit()  
    
    if mask=='24':
        lenPb = 254
        ipIniL = ipIniFin[0].split(".")
        ipMaxL = ipIniFin[1].split(".")
    
        ipIni = int(ipIniL[3])
        ipMax = int(ipMaxL[3])
        
        ip_addrB = ipIniL[0]+"."+ipIniL[1]+"."+ipIniL[2]+"."
    
    if mask=='32':
       print("The mask 32 has been selected")
       print("Sorry for the inconvenince. This feature is currently not working")
       sys.exit()
    
    portList = ports.split(",")
    
    print(portList)
    print()
    
    counter = 0
       
    openPorts = []
    closedPorts = []
    
    pb.printProgressBar(0, lenPb, prefix = 'Progress:', suffix = 'Complete', length = 60)
    
    while ipIni < ipMax:
        ip_addr = ip_addrB+str(ipIni)
        if verbose:
            print("IP: "+ip_addr+"                                                                                          ",end="\r\n")
            pb.printProgressBar(int(ipIni), lenPb, prefix = 'Progress:', suffix = 'Complete', length = 60)
        for port in portList:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                status = sock.connect_ex((ip_addr, int(port)))
                if status == 0:
                    if verbose:
                        print(f"Port: {port} - OPEN                                                                                       ", end="\r\n")
                    openPorts.append(port)
                else:
                    if verbose:
                        print(f"Port: {port} - CLOSED                                                                                       ", end="\r\n") #The free space is necesary in order to delete the previous output that was the progress bar
                    closedPorts.append(port)
                sock.close()
                # Update Progress Bar
                pb.printProgressBar(int(ipIni), lenPb, prefix = 'Progress:', suffix = 'Complete', length = 60)
            except socket.error as err:
                print(f"Connection error: {err}")    
                sys.exit()
        ipIni += 1
    print(f"\nOpen ports: {openPorts}")

#Scan a port for and IP
def ipPortScan(ip_addr, port, log, logOutput, dir_addr, verbose):
    pc.printout("\nDoing ping to the IP: "+ip_addr+"\n\n",pc.GREEN)
    
    openPorts = []
    closedPorts = []
    
    if log==True:
        if logOutput==None:
            if not os.path.exists(dir_addr+"/logs"):
                os.makedirs(dir_addr+"/logs")
            now = datetime.datetime.now()
            logging.basicConfig(filename=dir_addr+"/logs/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG)
        else:
           if not os.path.exists(logOutput):
                os.makedirs(logOutput)
           now = datetime.datetime.now()
           logging.basicConfig(filename=logOutput+"/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG)
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"Port: {port} - OPEN")
        else:
            print(f"Port: {port} - CLOSED")
    except socket.error as err:
        print(f"Connection error: {err}")    
        sys.exit()

def ipPortsScan(ip_addr, ports, log, logOutput, dir_addr, verbose):
    pc.printout("\nDoing ping to the IP: "+ip_addr+"\n",pc.GREEN)
    print("\nFor the ports: ")
    
    portList = ports.split(",")
    
    print(portList)
    print()
    
    openPorts = []
    closedPorts = []
    
    if log==True:
        if logOutput==None:
            if not os.path.exists(dir_addr+"/logs"):
                os.makedirs(dir_addr+"/logs")
            now = datetime.datetime.now()
            logging.basicConfig(filename=dir_addr+"/logs/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG)
        else:
           if not os.path.exists(logOutput):
                os.makedirs(logOutput)
           now = datetime.datetime.now()
           logging.basicConfig(filename=logOutput+"/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG)
    
    counter = 0
    
    pb.printProgressBar(counter, len(portList), prefix = 'Progress:', suffix = 'Complete', length = 60)
    
    for port in portList:
        try:
            int(port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            status = sock.connect_ex((ip_addr, int(port)))
            if status == 0:
                if verbose:
                    print(f"Port: {port} - OPEN                                                                                       ", end="\r\n")
                openPorts.append(port)
            else:
                if verbose:
                    print(f"Port: {port} - CLOSED                                                                                       ", end="\r\n") #The free space is necesary in order to delete the previous output that was the progress bar
                closedPorts.append(port)
            sock.close()
            counter += 1
            # Update Progress Bar
            pb.printProgressBar(counter, len(portList), prefix = 'Progress:', suffix = 'Complete', length = 60)
        except socket.error as err:
            print(f"Connection error: {err}")    
            sys.exit()
    print(f"\nOpen ports: {openPorts}")

def ipScan(ip_addr, log, logOutput, dir_addr, verbose):
    if log==True:
        if logOutput==None:
            if not os.path.exists(dir_addr+"/logs"):
                os.makedirs(dir_addr+"/logs")
            now = datetime.datetime.now()
            logging.basicConfig(filename=dir_addr+"/logs/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG)
        else:
           if not os.path.exists(logOutput):
                os.makedirs(logOutput)
           now = datetime.datetime.now()
           logging.basicConfig(filename=logOutput+"/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG) 
    pc.printout("\nDoing ping to the IP: "+ip_addr+"\n\n",pc.GREEN)
    
    port=1
    maxport=65536
    
    openPorts = []
    closedPorts = []
    
    pb.printProgressBar(0, maxport, prefix = 'Progress:', suffix = 'Complete', length = 60)
    
    while port < maxport:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            status = sock.connect_ex((ip_addr, port))
            if status == 0:
                if verbose:
                    print(f"Port: {port} - OPEN                                                                                       ", end="\r\n")
                openPorts.append(port)
            else:
                if verbose:
                    print(f"Port: {port} - CLOSED                                                                                       ", end="\r\n") #The free space is necesary in order to delete the previous output that was the progress bar
                closedPorts.append(port)
            sock.close()
            port += 1
            # Update Progress Bar
            pb.printProgressBar(port, maxport, prefix = 'Progress:', suffix = 'Complete', length = 60)
        except socket.error as err:
            print(f"Connection error: {err}")    
            sys.exit()
    print(f"\nOpen ports: {openPorts}")

#Scan all ports for ip_addr
def ipScanWmask(ip, mask, log, logOutput, dir_addr, verbose):
    
    if log==True:
        if logOutput==None:
            if not os.path.exists(dir_addr+"/logs"):
                os.makedirs(dir_addr+"/logs")
            now = datetime.datetime.now()
            logging.basicConfig(filename=dir_addr+"/logs/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG)
        else:
           if not os.path.exists(logOutput):
                os.makedirs(logOutput)
           now = datetime.datetime.now()
           logging.basicConfig(filename=logOutput+"/log-"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second), level=logging.DEBUG) 
    
    ipIniFin = ipv4calculator.ipv4calc(ip, mask, logging)
    
    print("\nThe ping will be done for the all the ports, for the IP "+ip+"\n")
    #f.write("\nThe ping will be done for the given ports, for the IP range from "+ipIniFin[0]+" to the IP "+ipIniFin[1]+" both included\n")
    
    #CALCULAR LA IP INI HASTA LA FINAL EJEMPLO (1 A 254 = 254 ips eso por la cantidad de puertos para sabes el porcentaje que hay que asignar a la progressbar
    
    lenPb=0
    
    if mask=='8':
       print("The mask 8 has been selected")
       print("Sorry for the inconvenince. This feature is currently not working")
       sys.exit() 
      
    if mask=='16':
       print("The mask 16 has been selected")
       print("Sorry for the inconvenince. This feature is currently not working")
       sys.exit()  
    
    if mask=='24':
        lenPb = 254
        ipIniL = ipIniFin[0].split(".")
        ipMaxL = ipIniFin[1].split(".")
    
        ipIni = int(ipIniL[3])
        ipMax = int(ipMaxL[3])
        
        ip_addrB = ipIniL[0]+"."+ipIniL[1]+"."+ipIniL[2]+"."
    
    if mask=='32':
       print("The mask 32 has been selected")
       print("Sorry for the inconvenince. This feature is currently not working")
       sys.exit()
       
    pc.printout("\nDoing ping to the IP: "+ip+"\n\n",pc.GREEN)
    
    port=1
    maxport=65536
    
    openPorts = []
    closedPorts = []
    
    #pb.printProgressBar(0, maxport, prefix = 'Progress:', suffix = 'Complete', length = 60)
    
    pb.printProgressBar(0, lenPb, prefix = 'Progress:', suffix = 'Complete', length = 60)
    
    while ipIni < ipMax:
        if verbose:
            ip_addr = ip_addrB+str(ipIni)
            print("IP: "+ip_addr+"                                                                                          ",end="\r\n")
            pb.printProgressBar(0, lenPb, prefix = 'Progress:', suffix = 'Complete', length = 60)
        while port < maxport:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                status = sock.connect_ex((ip_addr, port))
                if status == 0:
                    if verbose:
                        print(f"Port: {port} - OPEN                                                                                       ", end="\r\n")
                    openPorts.append(port)
                else:
                    if verbose:
                        print(f"Port: {port} - CLOSED                                                                                       ", end="\r\n") #The free space is necesary in order to delete the previous output that was the progress bar
                    closedPorts.append(port)
                sock.close()
                port += 1
                # Update Progress Bar
                pb.printProgressBar(int(ipIni), lenPb, prefix = 'Progress:', suffix = 'Complete', length = 60)
            except socket.error as err:
                print(f"Connection error: {err}")    
                sys.exit()
        ipIni += 1
    print(f"\nOpen ports: {openPorts}")
