from socket import socket
import sys, re

def scan_port(host_ip, port_list):




if __name__ == '__main__':
    if sys.argv.len == 4:
        if sys.argv[1] == '--host' and sys.argv[3] == '--port':
            if re.match('^(\d{1,3}\.){3}\d{1,3}$', sys.argv[2]) and re.match('\d+(-\d+)?', sys.argv[4]):
                host_ip = sys.argv[2]
                