# coding: utf-8

# @Time    : 2019/7/30 11:10 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 进程池-同步.py
# @Software: PyCharm

from multiprocessing import Pool
import os, time, random

def work(n):
    print "%s is running" % os.getpid()
    time.sleep(random.randint(1,3))
    return n**10

if __name__ == '__main__':
    p = Pool(5)
    result = []
    for i in range(1, 11):
        r = p.apply(func=work, args=(i,))
        result.append(r)
    print result
