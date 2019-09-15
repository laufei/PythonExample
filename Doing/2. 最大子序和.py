# coding: utf-8
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
	输入: [-2,1,-3,4,-1,2,1,-5,4],
	输出: 6
	解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""

def maxSubArray(nums):
    if len(nums) == 0:
        return 0
    for i in range(len(nums) - 1):
        nums[i + 1] = max(nums[i] + nums[i + 1], nums[i + 1])
    return max(nums)

print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))