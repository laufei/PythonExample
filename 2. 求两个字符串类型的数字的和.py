# coding: utf-8

# @Time    : 2019/8/5 11:51 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 求两个字符串类型的数字的和.py
# @Software: PyCharm

def plus(n1,n2):
    if len(n1) > len(n2):
        n1, n2 = n2, n1
    flag = 0
    total = ''
    try:
        for i in range(1, len(n2)+1):
            if i <= len(n1):
                j = int(n1[-i])+int(n2[-i])+flag
            else:
                j = int(n2[-i])+flag
            if j >= 10:
                flag = 1
            else:
                flag = 0
            total = str(j)[-1]+total
    except:
        print("%s和%s不能相加"%(n1,n2))
        return None

    if flag:
        total=str(flag)+total
    return total

assert plus('12399', '9999956')=='10012355'
assert plus('12399', '9956')=='22355'
assert plus('1n1','n11')==None