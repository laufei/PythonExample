# coding: utf-8
__author__ = 'liufei'
'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
# coding: utf-8
def fn(h, t):
    path = h
    high = h/2
    for i in range(t-1):
        path += high*2
        high = high/2
    return path, high

print fn(float(raw_input("请输入起始高度:")), int(raw_input("请输入反弹次数:")))