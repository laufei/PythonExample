# coding: utf-8

# @Time    : 2019/7/31 10:29 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 最长公共前缀.py
# @Software: PyCharm

'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入: ["flower","flow","flight"]
输出: "fl"
'''

def testFunc(strs):
    if not strs:
        return ""
    s1 = min(strs)
    s2 = max(strs)
    for i,x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print testFunc(strs)