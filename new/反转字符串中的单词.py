# coding: utf-8

# @Time    : 2019/8/27 9:20 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 反转字符串中的单词.py
# @Software: PyCharm

def reverStr(string):
    return " ".join([i[::-1] for i in string.split(" ")])


if __name__ == "__main__":
    string = "Let's take LeetCode contest"
    print reverStr(string)