# coding: utf-8
'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''
def fn():
    input = list(raw_input("请输入一个大于5位的数字："))
    lenght = len(input)
    if lenght < 5:
        exit("请输入一个大于5位的数字")
    for i in range(0, lenght/2):
        if input[i] != input[-(i+1)]:
            print "这不是个回文数"
            break
    else:
        print "这是个回文数"

fn()
