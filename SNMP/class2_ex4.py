
import argparse
from snmp_helper import snmp_get_oid,snmp_extract

parser = argparse.ArgumentParser('''SNMP function to collects sysName and sysDesc MIBs.
    Syntax is command IP_Address Community_String SNMP_Port''')
parser.add_argument("ip_addr")
parser.add_argument("comm_string")
parser.add_argument("snmp_port")
args = parser.parse_args()
ip_addr = args.ip_addr
comm_string = args.comm_string
snmp_port = args.snmp_port

def main():
    ''''
    Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
    prints out both the MIB2 sysName and sysDescr.
    '''
    a_device = (ip_addr, comm_string, snmp_port)

    snmp_sys_name = snmp_get_oid(a_device, oid='1.3.6.1.2.1.1.5.0')
    snmp_sys_desc = snmp_get_oid(a_device, oid='1.3.6.1.2.1.1.1.0')
    
    output_sys_name = snmp_extract(snmp_sys_name)
    output_sys_desc = snmp_extract(snmp_sys_desc)
    
    print '\nDevice Name:'
    print output_sys_name
    print '\nSystem Description:'
    print output_sys_desc + '\n'

if __name__ == '__main__':
    main()

