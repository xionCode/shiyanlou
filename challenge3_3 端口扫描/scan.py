from socket import socket
import sys, re

def get_argv():
    argv_list = sys.argv[1:]
    try:
        host_index = argv_list.index('--host')
        host_temp = argv_list[host_index + 1]
        port_index = argv_list.index('--port')
        port_temp = argv_list[port_index + 1]

        if re.match('^(\d{1,3}\.){3}\d{1,3}$', host_temp):
            host_ip = host_temp
        
        if re.match('\d+(-\d+)?', port_temp):
            port_list_num = [int(x) for x in port_temp.split('-')]
            if len(port_list_num) == 1:
                return host_ip, port_list_num
            else:
                port_list = [x for x in range(port_list_num[0], port_list_num[1]+1)]
                return host_ip, port_list
    except (ValueError, IndexError):
        print('Parameter Error')
        exit()

def scan_port(host_ip, port_list):
    for port in port_list:
        s = socket()
        s.settimeout(0.1)
        if s.connect_ex((host_ip, port)) == 0:
            print(port, 'open')
        else:
            print(port, 'closed')
        s.close()

if __name__ == '__main__':
    host_ip, port_list = get_argv()
    scan_port(host_ip, port_list)


