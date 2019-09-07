# coding: utf-8

# @Time    : 2019/8/5 11:42 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 合并两个有序列表为一个有序列表.py
# @Software: PyCharm

def merge(l1,l2):
    i1, i2 = 0, 0
    l = []
    try:
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] < l2[i2]:
                l.append(l1[i1])
                i1 += 1
            else:
                l.append(l2[i2])
                i2 += 1
            print i1, i2
        if i1 < len(l1):
            l.extend(l1[i1:])
        if i2 < len(l2):
            l.extend(l2[i2:])
    except:
        print('不能比较')
        return None
    return l

print(merge([1, 3, 3, 5, 6], [2, 4, 4, 6, 7]))