# coding: utf-8

def removeDuplicates(li):
    i = 0
    while i < len(li)-1:
        if li[i] == li[i+1]:
            li.remove(li[i])
        else:
            i += 1
    return li

st = removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(st)