#!/usr/bin/env python

import telnetlib
#Need the following to be able to use time.sleep
import time
#I need the following to be able to use try and except
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

#Create Telnet Connection
def telnet_connect(ip_addr):
	try:
		return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	except socket.timeout:
		sys.exit("Connection time-out")

#Login to the router rtr1
def login(remote_conn, username, password):
	output = remote_conn.read_until("sername", TELNET_TIMEOUT)
	remote_conn.write(username + '\n')
	output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
	remote_conn.write(password + '\n')
	return output

#Send command and return output
def send_command(remote_conn, cmd):
	#strip any trailing newlines
	cmd = cmd.rstrip()
	remote_conn.write(cmd + '\n')
	time.sleep(1)
	return remote_conn.read_very_eager()	
		
def main():
	#pynet-rtr1 (Cisco 881)
	ip_addr = '184.105.247.70'
	username = 'pyclass'
	password = '88newclass'
	
	#Create telnet connection to the router
	remote_conn = telnet_connect(ip_addr)
	
	#Login
	output = login(remote_conn, username, password)
	
	time.sleep(1)
	output = remote_conn.read_very_eager()
	
	#Disable paging
	remote_conn.write("terminal length 0" + '\n')
	
	#Send command and return output
	output = send_command(remote_conn, 'show ip int brief')
	print output
	
	remote_conn.close()
	
if __name__ == "__main__":
	main()
