# coding: utf-8

# @Time    : 2019/7/30 11:25 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 进程池-异步.py
# @Software: PyCharm

from multiprocessing import Pool
import os, time, random

def work(n):
    print "%s is running" % os.getpid()
    time.sleep(random.randint(1,3))
    return n**10

def save_to_file(r):
    with open("进程池-异步.txt", "a") as f:
        f.write(str(r)+"\n")

if __name__ == '__main__':
    p = Pool(5)
    result = []
    for i in range(1, 11):
        r = p.apply_async(func=work, args=(i,), callback=save_to_file)
        result.append(r)
    p.close()
    p.join()
    for j in result:
        print j.get()