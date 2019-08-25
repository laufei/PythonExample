# coding: utf-8

# @Time    : 2019/7/31 6:02 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 最长连续递增序列.py
# @Software: PyCharm

def testFun(list):
    list_len = len(list)
    if list_len < 2:
        return list_len
    count, tmp = 1, 1
    for i in range(list_len-1):
        if list[i] < list[i+1]:
            tmp += 1
            count = max(tmp, count)
        else:
            tmp = 1
    return count

if __name__ == "__main__":
    print testFun([21,22,23,1,2,3,4,6,5])