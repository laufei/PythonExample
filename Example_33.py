# coding: utf-8
__author__ = 'liufei'
'''
题目：按逗号分隔列表。
'''
a = [1,2,3,4,5]
b = ",".join(str(n) for n in a)
print b