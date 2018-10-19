#!/usr/bin/env python3
import sys, os.path, csv

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]

    def get_path(self, arg):
        index = self.args.index(arg) + 1
        path = self.args[index]
        if path:
#            if os.path.isfile(path):
#                return path
#            else:
#                print("parameter error")
#                exit()
            return path
        else:
            print("no parameter")

class Config(object):
    def __init__(self, cfgfile):
        self._config = {}
        with open(cfgfile, 'r') as f:
            for line in f:
                key, value = line.split('=')
                self._config[key.strip()] = value.strip()
        
    def get_config(self):
        return self._config

class UserData(object):
    def __init__(self, userdatafile):
        self._userdata = []
        with open(userdatafile, 'r') as f:
            self._userdata = list(csv.reader(f))
    
    def get_userdata(self):
        return self._userdata

class InComeTaxCalculator(object):
    def calc_for_all_userdata(self, cfgclass, udclass):
        self._result = []
        userdata = udclass.get_userdata()# list
        config = cfgclass.get_config()# dictionary
        # print(cfgclass.get_config('JiShuH'))
        for s in userdata:
            single = []
            for i in s:
                single.append(i)
            id = single[0]
            salary = int(single[1])
            premium = 0
            value = 0
            result = 0
            low = float(config['JiShuL'])
            high = float(config['JiShuH'])
            coefficient = float(config['YangLao']) + \
                float(config['YiLiao']) + \
                float(config['ShiYe']) + \
                float(config['GongShang']) + \
                float(config['ShengYu']) + \
                float(config['GongJiJin'])

            if salary < low:
                premium = low * coefficient
            elif salary > high:
                premium = high * coefficient
            else:
                premium = salary * coefficient
            single.append('{:.2f}'.format(premium))
            value = salary - 3500 - premium
            if value <= 1500:
                result = value * 0.03
            elif value <= 4500:
                result = value * 0.1 - 105
            elif value <= 9000:
                result = value * 0.2 - 1005
            elif value <= 35000:
                result = value * 0.25 - 1005
            elif value <= 55000:
                result = value * 0.3 - 2755
            elif value <= 80000:
                result = value * 0.35 - 5505
            else:
                result = value * 0.45 - 13505
            single.append('{:.2f}'.format(result))
            single.append('{:.2f}'.format(salary - premium - result))
            self._result.append(single)
        return self._result

    def export(self, result, path):
        with open(path, 'w') as f:
            csv.writer(f).writerows(result)
        

if __name__ == '__main__':
    arg = Args()
    config = Config(arg.get_path('-c'))
    userdata = UserData(arg.get_path('-d'))
    i = InComeTaxCalculator()
    result =  i.calc_for_all_userdata(config, userdata)
    i.export(result, arg.get_path('-o'))
    # print(config.get_config('JiShuH'))
    # print(userdata.get_userdata())

