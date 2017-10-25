# coding: utf-8
__author__ = 'liufei'
'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''
def fn(x, y):
    tmp = x
    result = 0
    for i in range(y):
        item = tmp
        result += item
        tmp = item*10+x
    return result

print fn(int(raw_input("请输入计算数字:")), int(raw_input("请输入循环次数:")))