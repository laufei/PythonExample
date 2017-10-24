# coding:utf-8
'''题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：'''

def fn(n):
    a, b = 0, 1
    result = [a]
    for i in range(n-1):
        a, b = b, a + b
        result.append(a)
    return result
print fn(36)