#!/usr/bin/env python3
import sys

def cal(salary):
    premium = salary * (0.08 + 0.02 + 0.005 + 0.06)
    value = salary - 3500 - premium
    result = 0
   
    if value <= 0:
        result = 0
    elif value <= 1500:
        result = value * 0.03
    elif value <= 4500:
        result = value * 0.1 - 105
    elif value <= 9000:
        result = value * 0.2 - 555
    elif value <= 35000:
        result = value * 0.25 - 1005
    elif value <= 55000:
        result = value * 0.3 - 2755
    elif value <= 80000:
        result = value * 0.35 - 5505
    else :
        result = value * 0.45 - 13505
    return salary - premium - result

if __name__ == '__main__':
    l =  sys.argv[1:]
    for i in l:
        key, value = i.split(':')
        try:
            result = cal(int(value))
        except ValueError:
            print("Parameter Error")
        print('{}:{:.2f}'.format(key, result))
