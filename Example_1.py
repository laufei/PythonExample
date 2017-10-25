# coding: utf-8
__author__ = 'liufei'

'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
'''

input = [1,2,3,4]
count = 0
for a in input:
    for b in input:
        for c in input:
            if a!=b!=c!=a:
                count+=1
                print a,b,c
print "count=",count
