# coding: utf-8

# @Time    : 2019/8/25 5:11 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : quicksort.py
# @Software: PyCharm

def quick_sort(l):
    llen = len(l)
    if llen < 2:
        return l
    mid = l[llen/2]
    l.remove(mid)
    left, right = [], []
    for i in l:
        if i > mid:
            right.append(i)
        else:
            left.append(i)
    return quick_sort(left) + [mid] + quick_sort(right)


def babble_sort(l):
    llen = len(l)
    if llen < 2:
        return l
    for i in range(llen-1):
        for j in range(i+1, llen):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

if __name__ == "__main__":
    l = [1, 2, 6, 4, 23, 3, 5]
    print babble_sort(l)
    print quick_sort(l)
