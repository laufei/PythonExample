# coding: utf-8
"""
给定一个m*n的二维列表，查找一个数是否存在。列表有下列特征：
1. 每一行的列表从左到右已经排序好；
2. 每一行第一个数比上一行最后一个数大。
[
    [1,3,5,7],
    [8,10,15,20],
    ...
    [80, 87, 93, 100]
]
"""

def fn(nums, target):
	i = 0
	max_i = len(nums) - 1
	j = len(nums[0]) - 1
	while i <= max_i and j >= 0:
		if nums[i][j] == target:
			return True
		elif nums[i][j] > target:
			j -= 1
		else:
			i += 1
	return False


nums = [
	[1, 3, 5, 7],
	[8, 10, 15, 20],
	[80, 87, 93, 100]
]
print(fn(nums, 15))
print(fn(nums, 14))


