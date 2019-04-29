# coding: utf-8

# @Time    : 2019/4/29 11:08 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : median-of-two-sorted-arrays.py
# @Software: PyCharm

# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        l = len(nums)
        if l == 1:
            return float(nums[0])
        if l % 2:
            return float(nums[l/2])
        else:
            return (float(nums[l/2]) + float(nums[l/2-1]))/2

a = [1]
b = [3, 4]
print Solution().findMedianSortedArrays(a, b)