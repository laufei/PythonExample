# coding: utf-8

# @Time    : 2019/7/30 3:40 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 队列Queue实现进程间通信.py
# @Software: PyCharm

from multiprocessing import Process, Queue
import time
# 向队列中写入数据
def work_1(q):
    try:
       n=1
       while n<20:
           print("work_1,%d"%n)
           q.put(n)
           time.sleep(1)
           n+=1
    except BaseException:
        print("work_1 error")
    finally:
       print("work_1 end!!!")

# 取出队列中的数据
def work_2(q):
    try:
       n=1
       while n<20:
            print("word_2,%d"%q.get())
            time.sleep(1)
            n+=1
    except BaseException:
       print("work_2 error")
    finally:
       print("work_2 end")

if __name__ == "__main__":
      q= Queue(8)
      p1=Process(target=work_1,args=(q,))
      p2=Process(target=work_2,args=(q,))
      p3=Process(target=work_2,args=(q,))
      p4=Process(target=work_2,args=(q,))
      p1.start()
      p2.start()
      p3.start()
      p4.start()
      p1.join()
      p2.join()
      p3.join()
      p4.join()
      print("all over")