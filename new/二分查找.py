# coding: utf-8

# @Time    : 2019/8/25 8:11 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 二分查找.py
# @Software: PyCharm
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # End Condition: left > right
        return -1