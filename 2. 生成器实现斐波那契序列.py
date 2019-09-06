# coding: utf-8

# @Time    : 2019/8/25 11:39 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 生成器实现斐波那契序列.py
# @Software: PyCharm

def gen_fib(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a+b
for i in gen_fib(10):
    print i,