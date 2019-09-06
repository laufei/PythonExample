# coding: utf-8

# @Time    : 2019/7/29 4:18 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 冒泡排序.py
# @Software: PyCharm

def testFun(l):
    slen = len(l)
    for i in range(slen-1):
        for j in range(i+1, slen):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    print l

testFun([1, 2, 6, 4, 23, 3, 5])

