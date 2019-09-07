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
    """
    :type A: List[int]
    :rtype: int
    """
    lmaxv = A[0]
    maxv = A[0]
    l = 0
    for i in range(len(A)):
        if A[i] < lmaxv:
            lmaxv = maxv
            l = i
        elif A[i] > maxv:
            maxv = A[i]
    return l + 1

A = [5,0,3,8,6]
print(partitionDisjoint(A))