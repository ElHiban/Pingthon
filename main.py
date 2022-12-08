#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:44:47 2022

@author: ivan
"""

import argparse
from src import printcolors as pc
from src import artwork
from methods import ping
import sys
import time
import os

def printlogo():
    pc.printout(artwork.ascii_art, pc.YELLOW)
    pc.printout("\nVersion BETA 1.0.0.0 - Developed by Iván Jurjo & Sergio Guitiérrez\n\n", pc.CYAN)
    pc.printout("Type '-h' or '--help' to show all allowed commands\n\n")

#print logo
printlogo()
 
#ARGUMENTS
    
parser = argparse.ArgumentParser(description='Pingthon is a simple tool that offers an interactive shell '
                                             'to perform ping to ips & ports manually or through a list')
parser.add_argument('-s', '--scan', metavar="IP",type=str, help='Asks for an IP in order to scan its ports, if the argument -p/--port or -P/--ports are not used, it will ask if scan all ports from 1 to 65535 both included', required=True)
parser.add_argument('-p', '--port', type=int, help='Add a port from the previous IP to scan')
parser.add_argument('-P', '--ports', type=str, help='Add a list of ports from the previous IP to scan. The format must be numbers separated with , and without spaces between them. An example could be: 1234,2345,3456,4567')
parser.add_argument('-m', '--mask', type=str, choices=['8', '16', '24', '32'], help='Add the submask for an IP in order to scan all the IPs in that range.')
parser.add_argument('-l', '--log', help='It creates a log where all the steps followed for your command are stored. If the argument -o/--output is not used, the log will be created on the same folder as the application, in a folder called Logs', action='store_true')
parser.add_argument('-o', '--output', type=str,help='Where to store the log, if argument -l/--log is not used, this option will be ignored')
parser.add_argument('-v', '--verbose', action="store_true", help='Shows every step that the program is doing through the console')
#parser.add_argument('-s', '--scan', help='username', action="store_true")
#parser.add_argument('-C','--cookies', help='clear\'s previous cookies', action="store_true")
#parser.add_argument('-j', '--json', help='save commands output as JSON file', action='store_true')
#parser.add_argument('-f', '--file', help='save output in a file', action='store_true')
#parser.add_argument('-c', '--command', help='run in single command mode & execute provided command', action='store')
#parser.add_argument('-o', '--output', help='where to store photos', action='store')

args = parser.parse_args()

dir_path = os.path.dirname(os.path.realpath(__file__))

#The option -p/--port will be deprecated the next update
if args.port:
    if args.mask:
        ping.IPSwMask4Port(args.scan, args.mask, args.port, args.log, args.output, dir_path, args.verbose)
    else:
        ping.ipPortScan(args.scan, args.port, args.log, args.output, dir_path, args.verbose)
else:
    if args.ports:
        #Functions IPSwMask4Ports and ipPortsScan merged into one for and optimous code??????
        if args.mask:
            ping.IPSwMask4Ports(args.scan, args.mask, args.ports, args.log, args.output, dir_path, args.verbose)
        else:
            ping.ipPortsScan(args.scan, args.ports, args.log, args.output, dir_path, args.verbose)
    else:
        allPorts = input("You did not add a port to scan, do you want to scan all ports from 1 to 65535 both included for that ip? [Y/N]: ")
        if allPorts=="Y" or allPorts=="y" or allPorts=="yes" or allPorts=="YES":
            if args.mask:
                ping.ipScanWmask(args.scan, args.mask, args.log, args.output, dir_path, args.verbose)
            else:
                ping.ipScan(args.scan, args.log, args.output, dir_path, args.verbose)
