# coding:utf-8
#冒泡排序

list = [1,2,6,5,11,23,9,10,4]
len = len(list)

for i in range(len):
    for j in range(i+1, len):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print list
