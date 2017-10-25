# coding: utf-8
__author__ = 'liufei'
'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
# coding: utf-8
def fn(h, t):
    route = h
    hight = route/2
    for i in range(1, t):
        if t == 1:
            break
        route += hight*2
        hight /= 2
    return route, hight

print fn(float(raw_input("请输入起始高度:")), int(raw_input("请输入反弹次数:")))
