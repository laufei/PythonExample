# coding: utf-8

# @Time    : 2019/8/27 9:57 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 找到所有数组中消失的数字.py
# @Software: PyCharm

def fn(nums):
    s = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in s]

nums = [4,3,2,7,8,2,3,1]
print fn(nums)