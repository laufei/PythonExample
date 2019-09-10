# coding: utf-8

# @Time    : 2019/8/3 9:08 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 检查IP有效性.py
# @Software: PyCharm

def testFunc(ip):
    ips_list = ip.split(".")
    ips_len = len(ips_list)
    if ips_len != 4:
        return False
    for i in ips_list:
        try:
            i = int(i)
        except:
            return False
        result = 256 > i >= 0
        if not result:
            return False
    return True

if __name__ == "__main__":
    ip0 = "10.1.11.1"
    ip1 = "10.1.1111.1"
    ip2 = "asdfasdf"
    ip3 = "a.b.c.d"
    ip4 = "10.0."
    ip5 = "10.1.1.1.1"
    ip6 = "10a.1.1.1i"
    ip7 = "10.1.1.10i"
    print testFunc(ip0)
    print testFunc(ip1)
    print testFunc(ip2)
    print testFunc(ip3)
    print testFunc(ip4)
    print testFunc(ip5)
    print testFunc(ip6)
    print testFunc(ip7)