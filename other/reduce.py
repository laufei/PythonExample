# coding: utf-8
__author__ = 'liufei'

l = [1, 3, 4, 5, 6, 7, 9]
print reduce(lambda x, y: x+y, l)
print l