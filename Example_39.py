# coding: utf-8
'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''

a = [2, 3, 5, 9, 23, 45, 56, 67, 98, 239]
input = int(raw_input("请输入一个整形数字:"))
a.append(input)
l = len(a)
for i in range(l-1, 0, -1):
    if a[i-1] > input:
        a[i], a[i-1] = a[i-1], a[i]
    else:
        break
print a

