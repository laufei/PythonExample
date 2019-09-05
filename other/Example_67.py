# coding: utf-8
__author__ = 'liufei'
'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''
# coding: utf-8
a = [1, 3, 5, 7, 21, 11, 2, 9]
print "原始:", a
s = sorted(a)
indexMax = a.index(s[-1])
a[indexMax], a[0] = a[0], a[indexMax]
print "最大的与第一个元素交换:", a
s = sorted(a)
indexMin = a.index(s[0])
a[indexMin], a[-1] = a[-1], a[indexMin]
print "最小的与最后一个元素交换:", a
