# coding: utf-8

"""
https://leetcode-cn.com/problems/nth-digit/solution/han-shu-er-fen-cha-zhao-by-iponder/
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

输入:11
输出:0
说明: 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
"""

def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """

    def func(x):
        if x == 0: return 0
        a = len(str(x))
        return x * a + a - sum(10**i for i in range(a))

    if n < 1:
        return

    left = 0
    right = 2 ** 31
    target = n
    mid = None
    found = False
    while left < right-1:
        mid = (left + right)//2
        mid_val = func(mid)
        if mid_val > target:
            right = mid
        elif mid_val < target:
            left = mid
        else:
            found = True
            break
    if found:
        return str(mid)[-1]
    if func(mid) > target:
        right = mid
    offset = func(right) - n
    return str(right)[-1-offset]

print(findNthDigit(987))