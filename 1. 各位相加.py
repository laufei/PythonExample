# coding: utf-8

# @Time    : 2019/8/27 10:49 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 各位相加.py
# @Software: PyCharm

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    result = 10
    while result > 9:
        a, b = num/10, num%10
        result = a + b
        num = result
    return result

print addDigits(38)