# coding: utf-8

# @Time    : 2019/8/27 11:42 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 单词拆分.py
# @Software: PyCharm

def wordBreak(s, wordDict):
    if not wordDict:
        return False

    max_sub_len = max([len(x) for x in wordDict])

    breakp = [0]

    for i in range(len(s) + 1):
        if i - breakp[0] > max_sub_len:
            breakp.pop(0)
            if not breakp:
                return False

        for j in breakp:
            if s[j:i] in wordDict:
                breakp.append(i)
                break

    return breakp[-1] == len(s)

s = "leetcode"
wordDict = ["leet", "code"]
print wordBreak(s, wordDict)