# coding: utf-8

# @Time    : 2019/8/5 11:51 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 判断一个字符串中的括号是否成对匹配.py
# @Software: PyCharm

def f1(s):
    start='{(['
    end='})]'
    cnt=[1,1,1]
    for i in s:
        if i in start:
            cnt[start.index(i)]+=1
        elif i in end:
            cnt[end.index(i)]-=1
        if not all(cnt):
            return False
    return all(cnt)
assert f1('[(u{u)]}')==True
assert f1('[(u{}u)]}')==False