# coding: utf-8
'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

def fn(x):
    a, b = 2.0, 1.0
    sum = 0
    for i in range(x):
        b, a = a, a + b
        sum += a/b
    return sum

print fn(20)

