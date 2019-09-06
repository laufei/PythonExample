# coding: utf-8

# @Time    : 2019/7/31 10:28 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 最长连续序列.py
# @Software: PyCharm

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp, count = 1, 1
        nums = sorted(list(set(nums)))
        nLen = len(nums)
        if nLen < 2:
            return nLen
        for i in range(nLen-1):
            if nums[i+1] == 1 + nums[i]:
                tmp += 1
                if tmp > count:
                    count = tmp
            else:
                tmp = 1
        return count

if __name__ == "__main__":
    l = [21,22,23,1,2,3,4,6,5]
    s = Solution()
    print (s.longestConsecutive(l))