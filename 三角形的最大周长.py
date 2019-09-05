# coding: utf-8

# @Time    : 2019/8/27 9:35 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 三角形的最大周长.py
# @Software: PyCharm

def fn(l):
    if len(l) < 3:
        return False
    l.sort(reverse=True)
    for i in range(len(l) - 2):
        if l[i] < l[i+1] + l[i+2]:
            return sum([l[i], l[i+1], l[i+2]])
    return False

l = [3,2,3,4]
print fn(l)