# coding: utf-8
"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：
	字母异位词指字母相同，但排列不同的字符串。
	不考虑答案输出的顺序。
	示例 1:
		输入:
		s: "cbaebabacd" p: "abc"

		输出:
		[0, 6]
	解释:
	起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
	起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
"""

def findAnagrams(s, p):

    # 思路:
    # 想象一个窗口在s上向右移动,窗口宽度为len(p)
    # 只要窗口内的字符串各字符数量与p中一致,则匹配成功
    # 窗口在向右移动的时候,只需要将最左端的值从字典中删除,将最右端+1的值加入字典即可.

    pmap = {}
    for i in p:
        pmap[i] = pmap.get(i,0) + 1
    plenth = len(p)

    rlist = []
    rmap = {}

    for i , v in enumerate(s):
        rmap[v] = rmap.get(v,0) + 1
        if rmap == pmap:
            rlist.append(i-plenth+1)
        if i - plenth + 1 >= 0:
            rmap[s[i-plenth + 1]] = rmap.get(s[i-plenth + 1]) - 1
            if rmap[s[i-plenth + 1]] == 0:
                del rmap[s[i-plenth + 1]]

    return rlist

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))