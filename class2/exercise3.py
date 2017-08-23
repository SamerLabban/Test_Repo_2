#!/usr/bin/env python

import telnetlib
import time
import socket
import sys
	
class rtr1_telnet_class(object):
	
	#Create Telnet Connection
	def telnet_connect(self, ip_addr, TELNET_PORT, TELNET_TIMEOUT):
		try:
			return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
		except socket.timeout:
			sys.exit("Connection time-out")

	#Login to the router rtr1
	def login(self, remote_conn, username, password, TELNET_TIMEOUT):
		output = remote_conn.read_until("sername", TELNET_TIMEOUT)
		remote_conn.write(username + '\n')
		output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
		remote_conn.write(password + '\n')
		return output

	#Send command and return output
	def send_command(self, remote_conn, cmd):
		#strip any trailing newlines
		cmd = cmd.rstrip()
		remote_conn.write(cmd + '\n')
		time.sleep(1)
		return remote_conn.read_very_eager()	
		
	def main(self):
		#pynet-rtr1 (Cisco 881)
		ip_addr = '184.105.247.70'
		username = 'pyclass'
		password = '88newclass'

		TELNET_PORT = 23
		TELNET_TIMEOUT = 6
		
		#Create telnet connection to the router
		remote_conn = self.telnet_connect(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
		
		#Login
		output = self.login(remote_conn, username, password, TELNET_TIMEOUT)
		
		time.sleep(1)
		output = remote_conn.read_very_eager()
		
		#Disable paging
		remote_conn.write("terminal length 0" + '\n')
		
		#Send command and return output
		output = self.send_command(remote_conn, 'show ip int brief')
		print output
		
		remote_conn.close()
	
if __name__ == "__main__":
	#Create an object of the above class
	class_object = rtr1_telnet_class()
	#Call functions in the above class
	class_object.main()

