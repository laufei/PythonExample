# coding: utf-8

def quick_sort(b):
    blen = len(b)
    if blen < 2:    #注意,使用递归算法, 这个判断必须要有
        return b
    mid = b[blen/2]
    left, right = [], []
    b.remove(mid)
    for i in b:
        if i > mid:
            right.append(i)
        else:
            left.append(i)
    return quick_sort(left) + [mid] + quick_sort(right)

list = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]
print quick_sort(list)