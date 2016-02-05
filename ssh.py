import paramiko
import time
from getpass import getpass

def disable_paging(session, command="terminal length 0\n", delay=1):

	session.send("\n")
	session.send(command)

	# Wait for the command to complete  
	time.sleep(delay)

	output = session.recv(65535)
	return output

def main():
	ip = "50.76.53.27"
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
	session.send("show version\n")

	# Wait for the command to complete  
	time.sleep(5)

	output = session.recv(65535)
	print output

	session_init.close()

if __name__ == "__main__":
	main()
