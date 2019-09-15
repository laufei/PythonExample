# coding: utf-8

def fn(nums):
    s = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in s]

nums = [4,3,2,7,8,2,3,1]
print fn(nums)