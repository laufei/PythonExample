# coding: utf-8

# @Time    : 2019/9/7 9:13 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 0. 数组的相对排序.py
# @Software: PyCharm

"""
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例:
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
"""
def relativeSortArray(arr1, arr2):
    arr2 += sorted(set(arr1)-set(arr2))
    arr1.sort(key=arr2.index)
    return arr1

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relativeSortArray(arr1, arr2))