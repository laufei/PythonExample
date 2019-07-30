# coding: utf-8
'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

def testFunc():
    a, b = 1.0, 1.0
    result = 0.0

    for i in range(20):
        a, b = a+b, a
        result += a/b
    return result

if __name__ == "__main__":
    print testFunc()


