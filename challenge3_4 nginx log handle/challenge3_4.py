# -*- coding: utf-8 -*-

import re 
from datetime import datetime

# 使用正则表达式解析日志文件，返回数据列表
def open_parser(filename):
    with open(filename) as logfile:
        # 使用正则表达式解析日志文件
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP 地址
                   r'\[(.+)\]\s'  # 时间
                   r'"GET\s(.+)\s\w+/.+"\s'  # 请求路径
                   r'(\d+)\s'  # 状态码
                   r'(\d+)\s'  # 数据大小
                   r'"(.+)"\s'  # 请求头
                   r'"(.+)"'  # 客户端信息
                   )
        parsers = re.findall(pattern, logfile.read())
    return parsers

def main():

    # 使用正则表达式解析日志文件
    logs = open_parser('nginx.log')

    '''
    1. 解析文件就是分离不同类型数据（IP，时间，状态码等）
    2. 从解析后的文件中统计挑战需要的信息
    '''
    ip_dict = {}
    url_dict = {}

    for log in logs:
        d = datetime.strptime(log[1], '%d/%b/%Y:%H:%M:%S +0800')
        if d.year == 2017 and d.month == 1 and d.day == 11:
            ip = log[0]
            if ip in ip_dict:
                ip_dict[ip] += 1
            else:
                ip_dict[ip] = 1

        if log[3] == '404':
            url = log[2]
            if url in url_dict:
                url_dict[url] += 1
            else:
                url_dict[url] = 1
        
        x1 = sorted(ip_dict.items(), key=lambda item : item[1])
        x2 = sorted(url_dict.items(), key=lambda item : item[1])
    return {x1[-1][0] : x1[-1][1]}, {x2[-1][0] : x2[-1][1]}


if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)