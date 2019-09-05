# coding: utf-8
'''
    对10个数进行排序。[5,3,23,67,2,56,45,98,239,9]
'''

a = [5,3,23,67,2,56,45,98,239,9]
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[j], a[i] = a[i], a[j]
print a

