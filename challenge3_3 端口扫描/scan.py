from socket import socket
import sys, re

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
    if len(sys.argv) == 5:
        if sys.argv[1] == '--host' and sys.argv[3] == '--port':
            if re.match('^(\d{1,3}\.){3}\d{1,3}$', sys.argv[2]) and re.match('\d+(-\d+)?', sys.argv[4]):
                host_ip = sys.argv[2]
                port_list_num = [int(x) for x in sys.argv[4].split('-')]
                if len(port_list_num) == 1:
                    scan_port(host_ip, port_list_num)
                else:
                    port_list = [x for x in range(port_list_num[0], port_list_num[1]+1)]
                    scan_port(host_ip, port_list)
            else:
                print('Parameter Error1')
        else:
            print('Parameter Error2')
    else:
        print('Parameter Error3')


