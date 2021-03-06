# coding: utf-8

# @Time    : 2019/9/7 9:23 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 0. 拼写单词.py
# @Software: PyCharm

"""
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。

示例 1：
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
"""

def countCharacters_1(words, chars):
    res = 0
    dict_chars = {}
    for i in chars:
        dict_chars[i] = dict_chars.get(i, 0) + 1
    for word in words:
        if all([dict_chars.get(w, 0) >= word.count(w) for w in word]):
            res += len(word)
    return res

import collections
def countCharacters_2(words, chars):
	res = 0
	cdict = collections.Counter(chars)
	for w in words:
		wdict = collections.Counter(w)
		if all([wdict[i] <= cdict.get(i, 0) for i in w]):
			res += len(w)
	return res

words = ["cat","bt","hat","tree"]
chars = "atach"
print(countCharacters_1(words, chars))
print(countCharacters_2(words, chars))