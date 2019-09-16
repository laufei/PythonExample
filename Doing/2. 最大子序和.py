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

def getMaxList(nums):
    nlen = len(nums)
    nmax = 0
    begin = 0
    end = 0
    for i in range(nlen - 1):
        tmp = nums[i]
        for j in range(i+1, nlen):
            tmp += nums[j]
            if nmax < tmp:
                nmax = tmp
                begin = i
                end = j
    return nums[begin: end + 1]
nums = [-4, 5, 8, -9, 12, -4, 0, 1]
print(getMaxList(nums))