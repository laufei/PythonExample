# coding: utf-8

# @Time    : 2019/9/5 8:58 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 二数之和.py
# @Software: PyCharm

def two_sum_1(li, num):
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == num:
                return i, j
    return False

def two_sum_2(li, num):
    tmp = {}
    for i in range(len(li)):
        a = li[i]
        b = num - a
        if b not in tmp:
            tmp[a] = i
        else:
            return tmp[b], i

li = [1, 3, 8, 5]
print two_sum_1(li, 13)
print two_sum_2(li, 13)