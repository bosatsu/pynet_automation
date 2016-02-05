

import pexpect
import sys
from getpass import getpass

def main ():
ip_addr = '50.76.53.27'
username = 'pyclass'
port = 8022
password = getpass()
ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
ssh_conn.logfile = sys.stdout
ssh_conn.timeout = 3
ssh_conn.expect('ssword:')
ssh_conn.sendline(password)
ssh_conn.expect('#')
print ssh_conn.before

if __name__ == '__main__':
	main()
