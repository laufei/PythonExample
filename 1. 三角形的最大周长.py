# coding: utf-8

def fn(l):
    l.sort(reverse=True)
    for i in range(len(l) - 2):
        if l[i] < l[i+1] + l[i+2]:
            return sum([l[i], l[i+1], l[i+2]])
    return False

l = [3,2,3,4]
print fn(l)