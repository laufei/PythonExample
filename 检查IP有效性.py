# coding: utf-8

# @Time    : 2019/8/3 9:08 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 检查IP有效性.py
# @Software: PyCharm

def testFunc(ip):
    ips_list = ip.split(".")
    ips_len = len(ips_list)
    if ips_len < 4:
        return False
    for i in ips_list:
        try:
            i = int(i)
        except:
            return False
        result = 256 > i > 0
    return result

if __name__ == "__main__":
    ip = "10.1.1"
    print testFunc(ip)