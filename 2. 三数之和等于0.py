# coding: utf-8

# @Time    : 2019/9/5 10:36 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 三数之和等于0.py
# @Software: PyCharm
'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
'''

def three_sum1(li):
    if len(li) < 3:
        return
    li.sort()
    res = set()
    for i in range(len(li) - 1):
        dic = {}
        for j in range(i + 1, len(li)):
            a = li[i]
            b = li[j]
            c = 0 - a - b
            if c not in dic:
                dic[a] = i
                dic[b] = j
            else:
                res.add((a, c, b))
    return map(list, res)

def three_sum2(li):
    if len(li) < 3:
        return
    li.sort()
    res = set()
    for i, v in enumerate(li[:-2]):
        d = {}
        for x in li[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))
    return map(list, res)

li = [-1, 0, 1, 2, -1, -4]
print three_sum1(li)
print three_sum2(li)