# coding: utf-8
__author__ = 'liufei'

input = 'beeeeegiiinnnnnnnn'
lenght = len(input)
print lenght
begin = 0
offset = 0
for i in range(lenght-1):
    print "i", i
    tmp = 0
    for j in range(i+1, lenght):
        print "j", j
        if input[i] == input[j]:
            tmp += 1
        if tmp > offset:
            begin = i
            offset = tmp
print "最长的字符串是: %s" % input[begin:begin+offset+1]
