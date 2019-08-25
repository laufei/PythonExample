# coding: utf-8

# @Time    : 2019/8/3 9:08 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 检查IP有效性.py
# @Software: PyCharm
import re

def testFunc(ip):
    ip_list= ip.split(".")
    ip_list_len = len(ip_list)
    if 4 != ip_list_len:
        return "非法IP"
    for i in ip_list:
        if not (re.match(r"\d{1,3}$", i) and int(i) < 255 and int(i) >=0) :
            return "非法IP"
        else:
            return "合法IP"

if __name__ == "__main__":
    ip1 = "10.1.1"
    ip2 = "asdfasdf"
    ip3 = "a.b.c.d"
    ip4 = "10.0."
    ip5 = "10.1.1.1.1"
    ip6 = "10a.1.1.i"
    ip7 = "10.1.1.10i"
    print testFunc(ip1)
    print testFunc(ip2)
    print testFunc(ip3)
    print testFunc(ip4)
    print testFunc(ip5)
    print testFunc(ip6)
    print testFunc(ip7)