# coding: utf-8
__author__ = 'liufei'

a = "aaaae3asdfda33333333333333334tadfllljdjjjjjjjjjjjjas033ad"
begin = 0
offset = 0

for i in range(len(a)-1):
    tmp = 0
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            tmp += 1
        else:
            break
        if tmp > offset:
            begin = i
            offset = tmp
print "最长的重复字符串是:%s, 其长度为:%d" % (a[begin:(begin+offset+1)], offset+1)

