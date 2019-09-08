# coding: utf-8
"""
https://leetcode-cn.com/problems/find-common-characters/
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。

示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
"""

def commonChars_1(A):
	res = []
	if not A:
		return res
	key = set(A[0])
	for k in key:
		minnum = min([a.count(k) for a in A])
		res += k*minnum
	return res

def commonChars_2(A):
	from collections import Counter
	from functools import reduce

	res = []
	d = reduce(lambda x,y: x & y, map(Counter, A))
	for k, v in d.items():
		res += [k] * v
	return res

s = ["bella", "label", "roller"]
print(commonChars_1(s))
print(commonChars_2(s))