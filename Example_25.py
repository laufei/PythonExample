# coding: utf-8
'''
题目：求1+2!+3!+...+20!的和。
'''
def jiechengFn(x):
    if x == 1:
        return 1
    else:
        return x*jiechengFn(x-1)

def sumFn(x):
    sum = 0L
    for i in range(1, x+1):
        sum += jiechengFn(i)
    return sum


print sumFn(20)

#=======================================#

def Fn(x):
    a = 1
    s = 0L
    for i in range(1, x+1):
        a *= i
        s += a
    return s
print Fn(20)