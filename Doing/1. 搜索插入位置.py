# coding: utf-8
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:
	输入: [1,3,5,6], 5
	输出: 2
示例 2:
	输入: [1,3,5,6], 2
	输出: 1
"""

def searchInsert(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return left

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))


