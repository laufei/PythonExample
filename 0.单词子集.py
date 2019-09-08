# coding: utf-8
"""
我们给出两个单词数组 A 和 B。每个单词都是一串小写字母。
现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称单词 b 是单词 a 的子集。 例如，“wrr” 是 “warrior” 的子集，但不是 “world” 的子集。
如果对 B 中的每一个单词 b，b 都是 a 的子集，那么我们称 A 中的单词 a 是通用的。
你可以按任意顺序以列表形式返回 A 中所有的通用单词。

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
输出：["facebook","google","leetcode"]
"""
def wordSubsets(A, B):
	def count(word):
		ans = [0] * 26
		for letter in word:
			ans[ord(letter) - ord('a')] += 1
		return ans

	bmax = [0] * 26
	for b in B:
		for i, c in enumerate(count(b)):
			bmax[i] = max(bmax[i], c)

	ans = []
	for a in A:
		if all(x >= y for x, y in zip(count(a), bmax)):
			ans.append(a)
	return ans

A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","o"]
print(wordSubsets(A, B))