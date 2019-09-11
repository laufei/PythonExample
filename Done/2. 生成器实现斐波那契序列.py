# coding: utf-8

def gen_fib(num):
    a, b = 0, 1
    for i in xrange(num):
        yield a
        a, b = b, a + b

for i in gen_fib(10):
    print i