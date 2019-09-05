# coding: utf-8

# @Time    : 2019/7/30 4:25 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 递归计算阶乘.py
# @Software: PyCharm

def testFunc(input):
    result = 1
    if input == 1:
        return 1
    else:
        result = input * testFunc(input-1)
    return result

if __name__ == "__main__":
    print testFunc(5)