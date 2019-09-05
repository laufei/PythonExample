#  coding: utf-8
'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''

def fn():
    input = str(raw_input("输入一个不多于5位的正整数"))
    l = len(input)
    rev = list(input)[::-1]
    print "长度：%s" % l, ", 逆序各位数字：", rev

fn()