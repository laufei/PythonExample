# coding: utf-8
__author__ = 'liufei'
'''
题目：求100之内的素数。
'''

def fn(x):
    for num in range(2, x+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print num

fn(100)