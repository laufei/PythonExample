# coding: utf-8

def removeDuplicates(shuzu):
    i = 0
    while i < len(shuzu)-1:
        if shuzu[i] == shuzu[i+1]:
            shuzu.remove(shuzu[i])
        else:
            i += 1
    return len(shuzu)

st = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(st)