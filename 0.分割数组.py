# coding: utf-8
"""
给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 left 和 right， 使得：

left 中的每个元素都小于或等于 right 中的每个元素。
left 和 right 都是非空的。
left 要尽可能小。
在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。

示例 1：
输入：[5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]
"""

def partitionDisjoint(A):
	if not A:
		return -1

	leftMax = A[0]
	allMax = A[0]
	l = 0
	for i in range(1, len(A)):
		allMax = max(allMax, A[i])
		if A[i] < leftMax:
			leftMax = allMax
			l = i
	return l + 1

A = [4, 0, 3, 5, 8, 6]
B = [3, 0, 5, 8, 6]
C = [0, 5, 3, 8, 6]
D = [32, 57, 24, 19, 0, 24, 49, 67, 87, 87]
print(partitionDisjoint(A))
print(partitionDisjoint(B))
print(partitionDisjoint(C))
print(partitionDisjoint(D))