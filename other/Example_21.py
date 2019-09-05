# coding: utf-8
__author__ = 'liufei'

'''
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''

def fn(x):
    tmp, result = 1, 0
    for _ in range(x-1):
        tmp = (tmp + 1) * 2
        result = tmp
    return result
print fn(10)