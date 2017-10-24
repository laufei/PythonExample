# coding:utf-8
#冒泡排序

list = [1,2,6,5,11,23,9,10,4]
len = len(list)

for i in range(len):
    for l in range(i+1, len):
        if list[l] > list[i]:
            tmp = list[l]
            list[l] = list[i]
            list[i] = tmp
print list

