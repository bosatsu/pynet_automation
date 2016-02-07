
import argparse
import paramiko
import time
from getpass import getpass

parser = argparse.ArgumentParser('''SSH function that takes 2 parameters.
	The first parameter should be an IP string to indicate which device .
	The second parameter should be a command string to be passed to the device.''')
parser.add_argument("ip_addr")
parser.add_argument("comm_string")
args = parser.parse_args()
ip_addr = args.ip_addr
comm_string = args.comm_string

def disable_paging(session, command="terminal length 0\n", delay=1):

	session.send("\n")
	session.send(command)

	# Wait for the command to complete  
	time.sleep(delay)

	output = session.recv(65535)
	return output

def main(ip, command):
	username = "pyclass"
	password = getpass()
	port = 8022
	
	session_init = paramiko.SSHClient()
	session_init.set_missing_host_key_policy(
		paramiko.AutoAddPolicy())

	session_init.connect(ip, username=username, password=password, port=port)
	session = session_init.invoke_shell()

	output = disable_paging(session)

	session.send("\n")
	session.send(command + "\n")

	# Wait for the command to complete  
	time.sleep(5)

	output = session.recv(65535)
	print output

	session_init.close()

if __name__ == "__main__":
	main(ip_addr, comm_string)
