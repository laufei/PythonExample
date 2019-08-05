# coding: utf-8

# @Time    : 2019/7/30 8:50 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 生产者消费者模式 - 协程.py
# @Software: PyCharm

from multiprocessing import Process
import time, random

def consumer():
    r = ''
    while True:
        n = yield r
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) #启动生成器
    n = 0
    while n < 5:
        n = n + 1
        # time.sleep(random.randint(1,3))
        print('[PRODUCER] Producing %s...' % n)
        t = c.send(n)
        print('[PRODUCER] Consumer return: %s' % t)
    c.close()

if __name__ == "__main__":
    c = consumer()
    ps = []
    for i in range(4):
        ps.append(Process(target=produce, args=(c,)))
    for p in ps:
        p.start()
        p.join()