# coding: utf-8

# @Time    : 2019/8/24 10:55 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : Test.py
# @Software: PyCharm

# coding: utf-8
__author__ = 'liufei'
# 1. 测试webdriver执行
'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://192.168.99.100:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)

driver.get("http://z.qyer.com")
print driver.execute_script("return window._RATrack")

driver.get("http://m.qyer.com/z")
print driver.execute_script("return window._RATrack")

driver.quit()
'''


# 2. 测试requests cookies的使用
'''
import requests
def find_out_all_url_httplib(startPageURL):
    session = requests.session()
    cookies = {
                "QYER_SHOP_AUTH": "e3deZD1wTaJFHKAMYI4fLb4LvNPbGEbtd2goL5OYcfp85wwJZ43nhbvDJHnul6%2BKs3WPys%2BHi2b5CHoDDsXLJE3LLi2k2Z3DAsOPMyD95Wshn%2BpndIZ07f0i%2BWdOzigVbGtL",
                "cdb_auth": "1d4865BHTGq2fiXekTGwM4a%2BxHpUvnaS7DTkVWLb2aTj6KmKKdZs7n8c9jiIp3FAx3bPRnOyAN5Z5CZv3QtlwmdlPrFR1A",
                "QYER_ADMIN_LOGIN_NEWX": "CDwNEWJ1CAtFKWV3cQ",
    }
    session.cookies = requests.utils.cookiejar_from_dict(cookies)
    response = session.get(startPageURL)
    html = response.text
    print "session.cookies.get_dict():", session.cookies.get_dict()
    print "html:", html
find_out_all_url_httplib("http://shop.qyer.com")
find_out_all_url_httplib("http://2b6.me")
'''

# 3. 测试登录方法
'''
import requests, json
from bs4 import BeautifulSoup as BS
def login_with_session(uid):
    reqURL = "http://soa.qyer.com/ucenter/user/synlogin?uid=%s" % uid
    try:
        response = requests.get(reqURL)
    except Exception, e:
        assert False, e
    script = json.loads(response.content)["data"]
    loginUrl = BS(script).findAll("script")[-1]["src"]
    s = requests.Session()
    r = s.get(loginUrl)
    if r.content != "":
        assert False, "Login Failed!"
    return s
print login_with_session("1316097").get("https://www.qyer.com/u/password").text
'''

# 4. 测试类属性
'''
class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, v):
        if not isinstance(v, int):
            raise ValueError('must be integer')
        if v < 0 or v > 100:
            raise ValueError('must between 0~100')
        self.__score = v

print Student.score
Student.score = "a"
print Student.score
'''

# 5. 测试字典拼接
'''
resultList = {}
a = ({'pid': 173657L, 'id': 4723601L}, {'pid': 173657L, 'id': 4721041L}, {'pid': 173657L, 'id': 4720436L}, {'pid': 173657L, 'id': 4718837L}, {'pid': 173657L, 'id': 4717463L}, {'pid': 173657L, 'id': 4717027L}, {'pid': 173657L, 'id': 4716748L}, {'pid': 173657L, 'id': 4716622L}, {'pid': 173657L, 'id': 4716373L}, {'pid': 173657L, 'id': 4716298L}, {'pid': 173657L, 'id': 4716213L}, {'pid': 173657L, 'id': 4715909L}, {'pid': 173657L, 'id': 4715092L}, {'pid': 173657L, 'id': 4714688L}, {'pid': 173657L, 'id': 4714333L}, {'pid': 173657L, 'id': 4714186L}, {'pid': 173657L, 'id': 4714163L}, {'pid': 173657L, 'id': 4713952L}, {'pid': 173657L, 'id': 4713795L}, {'pid': 173657L, 'id': 4713774L})
for row in a:
    for i in row.keys():
        tmp = []
        tmp.append(str(row.get(i)))
        resultList[i] = resultList.get(i, []) + tmp
print resultList
'''

# 6. 生成一定范围的URL
'''
for i in range(1000000, 1100000):
    with open("url.txt", "a+") as f:
        f.write("http://soa.qyer.ad/cash/account/moneyAdd POST uid=%d&event_id=16&money=0.6\n" % i)
'''

# 7. 测试多线程锁机制
'''
# coding : uft-8
import threading, time
class MyThread():
    n = 1
    def run(self, lock):
        time.sleep(1)
        if lock.acquire():
            print self.n, threading.Thread
            self.n += 1
            lock.release()

if "__main__" == __name__:
    ThreadList = []
    lock = threading.Lock()
    mt = MyThread()
    for i in range(1, 200):
        t = threading.Thread(target=mt.run, args=(lock,))
        ThreadList.append(t)
    for t in ThreadList:
        t.start()
    for t in ThreadList:
        t.join()
'''

# 8. 测试python-jenkins库
'''
import jenkins, requests
JENKINS_SERVER_URL = "http://172.1.9.103:8080"
JENKINS_API_URL = JENKINS_SERVER_URL + "/job/%s/api/json"

def get_jenkins_job_status(job_name, num):
    server=jenkins.Jenkins(JENKINS_SERVER_URL)
    print server.get_running_builds()
    # print server.get_build_console_output(job_name, num)
    print server.get_build_info(job_name, num)

get_jenkins_job_status("api_open_biu", 6556)

def latest_build(job_name):
    response = requests.get(JENKINS_API_URL % job_name)
    url = response.json().get("builds")[0].get("url")
    return url
print latest_build("api_open_biu")
'''

# 9. 测试requests cookies数据是否也是放在headers里
'''
# Install the Python Requests library:
# `pip install requests`

import requests
def send_request():
    # My API
    # GET http://www.2b6.me/user/user.php

    try:
        response = requests.get(
            url="http://www.2b6.me/user/user.php",
            params={
                "stype": 1,
                "uid": 1,
            },
            headers={
                "Cookie": "QYER_ADMIN_LOGIN_NEWX=CDwNEWJ1CAtFKWV3cQ",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
send_request()
'''

# 10. 冒泡排序
'''
def bubble_sort(list):
    l = len(list)
    for i in range(l-1):
        for j in range(1+i, l):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

import random
l = []
for i in range(50):
    l.append(random.randrange(100))
print bubble_sort(l)
'''

# 11. Mock测试
'''
'''
# 12. celery测试
'''
'''

# 13. 多进程加锁测试1
'''
from multiprocessing import Process,Lock
import time,random
#互斥锁：必须是lock.acquire()一次，然后lock.release()释放一次，才能继续lock.acquire()
#互斥锁和join区别
#大前提：二者的原理都是一样的，都是将并发变成串行，从而保证有序
#区别：join是按照认为指定的顺序执行，而互斥锁是所有的进程平等的竞争，谁先抢到谁执行
mutex=Lock()
def task1(lock):
    lock.acquire()#接受一次
    print('task1:名字是wss')
    time.sleep(random.randint(1,3))
    print('task1:性别是male')
    time.sleep(random.randint(1, 3))
    print('task1:年龄是18')
    lock.release()#释放一次
def task2(lock):
    lock.acquire()#接受一次
    print('task2:名字是qss')
    time.sleep(random.randint(1,3))
    print('task2:性别是male')
    time.sleep(random.randint(1, 3))
    print('task2:年龄是48')
    lock.release()#释放一次
def task3(lock):
    lock.acquire()#接受一次
    print('task3:名字是lss')
    time.sleep(random.randint(1,3))
    print('task3:性别是fmale')
    time.sleep(random.randint(1, 3))
    print('task3:年龄是38')
    lock.release()#释放一次
if __name__=='__main__':
    p1=Process(target=task1,args=(mutex,))
    p2=Process(target=task2,args=(mutex,))
    p3=Process(target=task3,args=(mutex,))
    p3.start()
    p3.join()
    p1.start()
    p1.join()
    p2.start()
    p2.join()
'''

# 14. 多进程加锁测试2
'''
import time
import random
import os
from multiprocessing import Process,Lock
mutex=Lock()
# 互斥锁vs join的区别一：
# 互斥锁可以让一部分代码（修改共享数据的代码）串行，而join只能将代码整体串行
def search():
    time.sleep(random.randint(1,3))
    with open('test.tmp','r') as f:
        count = f.read()
        print '%s 剩余票数:%s' % (os.getpid(), count)

def get():
    with open('test.tmp','r') as f:
        count = f.read()
    if int(count) > 0:
        count = int(count) - 1
        time.sleep(random.randint(1,3))#模拟网络延迟
        with open('test.tmp','w') as f:
            f.write(str(count))
        print('%s 购票成功' %os.getpid())

def task(lock):
    search()
    lock.acquire()
    get()
    lock.release()

if __name__ == '__main__':
    for i in range(10):
        p=Process(target=task,args=(mutex,))
        p.start()
        # p.join()
'''

# 15. 多进程信号量测试
'''
from multiprocessing import Process,Semaphore
import time,random

def go_ktv(sem,user):
    sem.acquire()
    print('%s 占到一间ktv小屋' %user)
    time.sleep(random.randint(0,1)) #模拟每个人在ktv中待的时间不同
    sem.release()
    print('release')

if __name__ == '__main__':
    sem=Semaphore(4)
    p_l=[]
    for i in range(13):
        p=Process(target=go_ktv,args=(sem,'user%s' %i,))
        p.start()
        p_l.append(p)

    for i in p_l:
        i.join()
    print('============》')
'''

# 16. 多进程事件测试
'''
from multiprocessing import Process, Event
import time, random

def car(e, n):
    while True:
        if not e.is_set():  # 进程刚开启，is_set()的值是Flase，模拟信号灯为红色
            print('\033[31m红灯亮\033[0m，car%s等着' % n)
            e.wait()    # 阻塞，等待is_set()的值变成True，模拟信号灯为绿色
            print('\033[32m车%s 看见绿灯亮了\033[0m' % n)
            time.sleep(random.randint(3, 6))
            if not e.is_set():   #如果is_set()的值是Flase，也就是红灯，仍然回到while语句开始
                continue
            print('车开远了,car', n)
            break


def police_car(e, n):
    while True:
        if not e.is_set():# 进程刚开启，is_set()的值是Flase，模拟信号灯为红色
            print('\033[31m红灯亮\033[0m，car%s等着' % n)
            e.wait(0.1) # 阻塞，等待设置等待时间，等待0.1s之后没有等到绿灯就闯红灯走了
            if not e.is_set():
                print('\033[33m红灯,警车先走\033[0m，car %s' % n)
            else:
                print('\033[33;46m绿灯，警车走\033[0m，car %s' % n)
        break

def traffic_lights(e, inverval):
    while True:
        time.sleep(inverval)
        if e.is_set():
            print('######', e.is_set())
            e.clear()  # ---->将is_set()的值设置为False
        else:
            e.set()    # ---->将is_set()的值设置为True
            print('***********',e.is_set())

if __name__ == '__main__':
    e = Event()
    for i in range(10):
        p=Process(target=car,args=(e,i,))  # 创建是个进程控制10辆车
        p.start()

    for i in range(5):
        p = Process(target=police_car, args=(e, i,))  # 创建5个进程控制5辆警车
        p.start()
    t = Process(target=traffic_lights, args=(e, 10))  # 创建一个进程控制红绿灯
    t.start()

    print('============》')
'''

# 17. 进程池测试 - 同步
'''
import os,time
from multiprocessing import Pool

def work(n):
    print('%s run' %os.getpid())
    time.sleep(3)
    return n**2

if __name__ == '__main__':
    p=Pool(3) #进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l=[]
    for i in range(10):
        res=p.apply(work,args=(i,)) # 同步调用，直到本次任务执行完毕拿到res，等待任务work执行的过程中可能有阻塞也可能没有阻塞
                                    # 但不管该任务是否存在阻塞，同步调用都会在原地等着
        res_l.append(res)
    print(res_l)
'''

# 18. 进程池测试 - 异步
'''
import os
import time
import random
from multiprocessing import Pool

def work(n):
    print('%s run' %os.getpid())
    time.sleep(random.random())
    return n**2

if __name__ == '__main__':
    p=Pool(3) #进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l=[]
    for i in range(10):
        res=p.apply_async(work,args=(i,)) # 异步运行，根据进程池中有的进程数，每次最多3个子进程在异步执行
                                          # 返回结果之后，将结果放入列表，归还进程，之后再执行新的任务
                                          # 需要注意的是，进程池中的三个进程不会同时开启或者同时结束
                                          # 而是执行完一个就释放一个进程，这个进程就去接收新的任务。
        res_l.append(res)

    # 异步apply_async用法：如果使用异步提交的任务，主进程需要使用join，等待进程池内任务都处理完，然后可以用get收集结果
    # 否则，主进程结束，进程池可能还没来得及执行，也就跟着一起结束了
    p.close()
    p.join()
    for res in res_l:
        print(res.get()) #使用get来获取apply_aync的结果,如果是apply,则没有get方法,因为apply是同步执行,立刻获取结果,也根本无需get
'''

# 19. 进程池测试 - 异步带回调函数
'''
from multiprocessing import Pool
import requests
import json
import os

def get_page(url):
    print('<进程%s> get %s' %(os.getpid(),url))
    respone=requests.get(url)
    if respone.status_code == 200:
        return {'url':url,'text':respone.text}

def pasrse_page(res):
    print('<进程%s> parse %s' %(os.getpid(),res['url']))
    parse_res='url:<%s> size:[%s]\n' %(res['url'],len(res['text']))
    with open('db.txt','a') as f:
        f.write(parse_res)


if __name__ == '__main__':
    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    p=Pool(3)
    res_l=[]
    for url in urls:
        res=p.apply_async(get_page,args=(url,),callback=pasrse_page)
        res_l.append(res)

    p.close()
    p.join()
'''

# 20. 队列Queue实现进程间通信
'''
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
      q= Queue()
      p1=Process(target=work_1,args=(q,))
      p2=Process(target=work_2,args=(q,))
      p1.start()
      p2.start()
      p1.join()
      p2.join()
      print("all over")
'''

# 21. 二叉树遍历测试 - 递归算法
'''
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left                #左子树
        self.right = right           #右子树

def preTraverse(root):
    # 前序遍历
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def midTraverse(root):
    # 中序遍历
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)


def afterTraverse(root):
    # 后序遍历
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)

if __name__ == '__main__':
    root = Node(
        value='D',
        left=Node(
            value='B',
            left=Node('A'),
            right=Node('C')
        ),
        right=Node(
            value='E',
            right=Node(
                value='G',
                left=Node('F')
            )
        )
    )
    print('前序遍历：')
    preTraverse(root)
    print('\n')
    print('中序遍历：')
    midTraverse(root)
    print('\n')
    print('后序遍历：')
    afterTraverse(root)
    print('\n')
'''

# 22. 已知二叉树的前序遍历和中序遍历，求这棵二叉树的后序遍历
'''
preList = list('12473568')
midList = list('47215386')
afterList = []

def findTree(preList, midList, afterList):
    if len(preList) == 0:
        return
    if len(preList) == 1:
        afterList.append(preList[0])
        return
    root = preList[0]
    n = midList.index(root)
    findTree(preList[1:n + 1], midList[:n], afterList)
    findTree(preList[n + 1:], midList[n + 1:], afterList)
    afterList.append(root)
    return afterList

print findTree(preList, midList, afterList)
'''

# 23. 已知二叉树的后序遍历和中序遍历，求这棵二叉树的前序遍历
'''
preList = []
midList = list('47215386')
afterList = list('74258631')

def findTree(preList, midList, afterList):
    if len(afterList) == 0:
        return
    if len(afterList) == 1:
        preList.append(afterList[0])
        return
    root = afterList[-1]
    n = midList.index(root)
    findTree(afterList[1:n + 1], midList[:n], preList)
    findTree(afterList[n + 1:], midList[n + 1:], preList)
    preList.append(root)
    return preList

print findTree(preList, midList, afterList)
'''

# 24. Python编程实现二叉树及七种遍历方法
'''
# ① 树的构造
# ② 递归实现先序遍历、中序遍历、后序遍历
# ③ 堆栈实现先序遍历、中序遍历、后序遍历
# ④ 队列实现层次遍历

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1: # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0] # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0) # 如果该结点存在右子树，将此结点丢弃。

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print root.elem,
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                print node.elem,
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild                 #开始查看它的右子树

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print root.elem,
        self.middle_digui(root.rchild)

    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            print node.elem,
            node = node.rchild                 #开始查看它的右子树

    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print root.elem,

    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                    #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
            print myStack2.pop().elem,

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print node.elem,
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

if __name__ == '__main__':
    """主函数"""
    elems = range(10)            #生成十个数据作为树节点
    tree = Tree()         #新建一个树对象
    for elem in elems:
        tree.add(elem)            #逐个添加树的节点
    print '队列实现层次遍历:'
    tree.level_queue(tree.root)
    print '\n\n递归实现先序遍历:'
    tree.front_digui(tree.root)
    print '\n递归实现中序遍历:'
    tree.middle_digui(tree.root)
    print '\n递归实现后序遍历:'
    tree.later_digui(tree.root)
    print '\n\n堆栈实现先序遍历:'
    tree.front_stack(tree.root)
    print '\n堆栈实现中序遍历:'
    tree.middle_stack(tree.root)
    print '\n堆栈实现后序遍历:'
    tree.later_stack(tree.root)
'''

# 25. 递归计算阶乘
'''
def jiecheng(value):
    if value == 1:
        return 1
    else:
        return value*jiecheng(value-1)
print jiecheng(6)
'''

# 26. 正则基础
'''
import re
# 1) re.match
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# 2)
# re.MatchObject
# group() 返回被 RE 匹配的字符串。
# start() 返回匹配开始的位置
# end() 返回匹配结束的位置
# span() 返回一个元组包含匹配 (开始,结束) 的位置

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

# 3) re.search
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
line = "Cats are smarter than dogs";

 # 4)
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"

# 5) re.sub
phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num
# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num

# 6) re.sub
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

# 7) re.compile
# re.RegexObject
# re.compile() 返回 RegexObject 对象。
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配s
print m.group(0)   # 可省略 0
print m.start(0)   # 可省略 0
print m.end(0)     # 可省略 0
print m.span(0)    # 可省略 0

# 8) re.findall
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print result1
print result2

# 9) re.finditer
pattern = re.compile(r'\d+')   # 查找数字
it = pattern.finditer("12a32bc43jf3")
for match in it:
    print (match.group())

# 10) re.split
print re.split('\W+', 'runoob, runoob, runoob.')
print re.split('(\W+)', ' runoob, runoob, runoob.')
print re.split('\W+', ' runoob, runoob, runoob.', 1)
print re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
'''

# 27. 正则练习
'''
import re
str = "12233asdf990q234lllasdf23000_992A##"
sco = re.compile(r'\d{5}')
print sco.findall(str)
sco1 = re.compile(r'\w+')
print sco1.findall(str)
date = "2016-12-12 14:34"
dco = re.compile(r"(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2})")
print dco.match(date).group()
'''

# 28. 生成器 & 迭代器练习
'''
# 生成器: 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# python中生成器是迭代器的一种，使用yield返回值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。

l = [1, 2, 3, 4, 5, 6, 7, 8]
ll = map(lambda x: x+2, l )
lll = reduce(lambda x,y: x*y, l)
llll = [i+2 for i in l]
print ll
print lll
print llll

generator = (i+2 for i in l)
print generator.next()
print generator.send(i)
print next(generator)
print '---------'
for i in generator:
    print i

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print(g.send(44))

def fib():
    i = 10
    a, b = 1, 1
    while i > 0:
        i -= 1
        yield a, b
        a, b = b, a+b

fib = fib()
for i in range(20):
    try:
        print fib.next()
    except StopIteration as e:
        break
'''

# 29. 大文本处理练习
'''
def readInChunks(fileObj, chunkSize=4096):
    while 1:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

with open('bigFile') as f:
    for chuck in readInChunks(f):
        # dosomething here...
        print chuck
'''


# 30. 大文本处理练习: 多线程, 队列, 线程池的应用
'''
import threading
import ConfigParser
import url_func
import sys
import Queue


class Reader(threading.Thread):
    def __init__(self, thread_id):
        super(Reader, self).__init__()
        self.thread_id = thread_id

    def run(self):
        global q

        temp_list = q.get()

        for text in temp_list:
            columns = text.split('\001')
            if len(columns) == 8:
                #取出线程对应文件内容后的文件操作,可忽略
                url_func.url_make_open(a_o_b, plat_form, self.thread_id, columns)


class Partition(object):
    def __init__(self, file_name, thread_num):
        self.file_name = file_name
        self.block_num = thread_num

    #按照线程数对文件进行分块并存进queue中
    def part_and_queue(self):
        pos_list = []
        #文件总行数
        file_size = url_func.file_lines(self.file_name)
        #按照线程数分成对应块的大小
        block_size = file_size / self.block_num
        start_pos = 0
        global q

        for i in range(self.block_num):
            if i == self.block_num - 1:
                end_pos = file_size - 1
                pos_list.append((start_pos, end_pos))
                break
            end_pos = start_pos + block_size - 1
            if end_pos >= file_size:
                end_pos = file_size - 1
            if start_pos >= file_size:
                break
            pos_list.append((start_pos, end_pos))
            start_pos = end_pos + 1

        #读取每块内容存进queue中
        fd = open(self.file_name, 'r')
        for pos_tu in pos_list:
            temp_text = []
            start = pos_tu[0]
            end = pos_tu[1]

            while start <= end:
                text = fd.readline().strip('\n')
                temp_text.append(text)
                start = start + 1

            q.put(temp_text)
        fd.close()


if __name__ == '__main__':

    config = ConfigParser.ConfigParser()
    config.readfp(open('config'))
    file_name = sys.argv[1]
    plat_form = sys.argv[2]
    a_o_b = sys.argv[3]

    #线程数量可配
    thread_num = int(config.get('info', 'threadNum'))
    q = Queue.Queue()
    p = Partition(file_name, thread_num)
    t = []
    p.part_and_queue()

    for i in range(thread_num):
        t.append(Reader(i))
    for i in range(thread_num):
        t[i].start()
    for i in range(thread_num):
        t[i].join()
'''

# 31. 字典排序
'''
from collections import OrderedDict
dict = {
            8: {'k': 8, 'v': 'eight'},
            2: {'k': 2, 'v': 'two'},
            1: {'k': 1, 'v': 'one'},
            10: {'k': 10, 'v': 'ten'},
}
print dict.items()
result = OrderedDict(sorted(dict.items(), key=lambda t: t[0]))
print type(result)
print result.items()
'''

# 32. python实现数据结构 - 栈
'''
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, v):
        self.items.append(v)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

s = Stack()
print s.isEmpty()
s.push(1)
s.push(3)
print s.peek()
print s.size()
s.pop()
print s.size()
s.pop()
if not s.isEmpty():
    s.pop()
else:
    print "s is empty"
'''

# 33. python实现数据结构 - 队列
'''
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, v):
        self.items.insert(0, v)

    def dequeue(self):
        self.items.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.isEmpty()
q.dequeue()
print q.size()
q.dequeue()
q.dequeue()
print q.isEmpty()
'''

# 34. python实现数据结构 - 单向链表
'''
class Node():
    __slots__ = ['_item','_next']
    def __init__(self,item):
        self._item = item
        self._next = None

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setItem(self, newitem):
        self._item = newitem

    def setNext(self, newnext):
        self._next = newnext

class SingleLinkedList():
    def __init__(self):
        self._head = None  #初始化为空链表

    # 是否为空
    def isEmpty(self):
        return self._head == None

    # 链表长度
    def size(self):
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    # 遍历链表
    def travel(self):
        current = self._head
        while current != None:
            print current.getItem()
            current = current.getNext()

    # 头部新增节点
    def add(self, item):
        temp = Node(item)
        temp.setNext(self._head)
        self._head = temp

    # 尾部新增节点
    def append(self, item):
        temp = Node(item)
        if self.isEmpty():
            self._head = temp   #若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()   #遍历链表
            current.setNext(temp)   #此时current为链表最后的元素

    # 是否存在某个节点数据
    def search(self, item):
        current = self._head
        founditem = False
        while current != None:
            if current.getItem() == item:
                founditem = True
                break
            else:
                current = current.getNext()
        return founditem

    # 某个节点数据的位置
    def index(self, item):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getItem() == item:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            raise ValueError, '%s is not in linkedlist' % item

    # 删除某个节点
    def remove(self, item):
        current = self._head
        pre = None
        while current != None:
            if current.getItem() == item:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    # 在某个位置插入节点
    def insert(self, pos, item):
        if pos <= 1:
            self.add(item)
        elif pos > self.size():
            self.append(item)
        else:
            temp = Node(item)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)

if __name__ == '__main__':
    a=SingleLinkedList()
    for i in range(1,10):
        a.append(i)
    print a.size()
    a.travel()
    print a.search(6)
    print a.index(5)
    a.remove(4)
    a.travel()
    a.insert(4,100)
    a.travel()
'''

# 35. 二分查找
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # End Condition: left > right
        return -1
'''

# 36. x 的平方根
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

if __name__ == "__main__":
    print Solution().mySqrt(8)

'''

# 37.
'''
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''

#38.
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

'''
# 39.
'''
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''

# 40.
'''
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue(4)
    pw = Process(target=write, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    pr = Process(target=read, args=(q,))
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
'''

# 41.
'''
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
'''

# 42.

'''
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
'''

# 43.
'''
import re
print re.split(r"[\s\,\;]+", "a,b;; c  d")


from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1']
print dd['key2']
'''

# 44.
'''
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) #启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        t = c.send(n)
        print('[PRODUCER] Consumer return: %s' % t)
    c.close()

c = consumer()
produce(c)
'''

# 45. 动态添加属性及方法
'''
class Persion(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print "My name is %s, and %d years old!" % (self.name, self.age)

p = Persion("Luca", 37)
#新增属性
p.sex = "male"
print "My sex is %s" % p.sex

def eat(self):
    print "I'm eatting!"

from types import MethodType
p.eat = MethodType(eat, p)
p.eat()
'''

# 46. 协程小栗子
'''
def test1():
    while True:
        print "_____1____"
        yield

def test2():
    while True:
        print "_____2____"
        yield
t1 = test1()
t2 = test2()
while True:
    next(t1)
    next(t2)
'''

# 47. Process()
'''
from multiprocessing import Process
import time
def test():
    for i in range(5):
        print "-----1-----"
        time.sleep(1)

p = Process(target=test)
p.start()
p.join()            #堵塞
print "----main----"
'''

# 48. Process子类创建进程
'''
from multiprocessing import Process
import time, os

class prcsTest(Process):
    def __init__(self, gap):
        Process.__init__(self)
        self.gap = gap

    def work(self, index):

        print "[%d]PID: %s" % (index, os.getpid())

    def run(self):
        self.work(2)
        for i in range(5):
            print "-----1-----"
            time.sleep(self.gap)

pt = prcsTest(1)
pt.start()
pt.join(3)
print "----main----"
'''

# 49. Pool()测试
'''
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
'''

# 50. Queue()测试
'''
from multiprocessing import Queue, Process
import random, time, os

def writer(q):
    for i in ["a", "b", "c"]:
        if not q.full():
            q.put(i)
            print "%s被放入队列" % i
            time.sleep(random.random())

def reader(q):
    while True:
        if not q.empty():
            r = q.get()
            print "%s被取出队列" % r
            time.sleep(random.random())
        else:
            break

q = Queue(6)
for i in range(5):
    pw = Process(target=writer, args=(q,))
    pr = Process(target=reader, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print "进程%s执行完成!" % os.getpid()
'''

# 51. 批量copy文件夹下的文件到另一个文件夹下
'''
import os, time
from multiprocessing import Pool, Manager

def copy_file(filename, folder_path, new_folder_name, queue):
    old = folder_path+os.sep+filename
    new = new_folder_name+os.sep+filename
    if os.path.exists(new):
        os.rmdir(new)
        print "%s文件夹存在, 并已删除!"

    with open(old, "rb") as fr:
        frc = fr.read()
        with open(new, "wb") as fw:
            fw.write(frc)
    queue.put(filename)

def main():
    folder_path = raw_input("请输入文件夹的路径:")
    filenames = os.listdir(folder_path)
    new_folder_name = folder_path + "_new"
    if os.path.exists(new_folder_name):
        os.system("rm -rf %s" % new_folder_name)
        print "%s文件夹存在, 并已删除!" % new_folder_name
    os.mkdir(new_folder_name)

    p = Pool(5)
    q = Manager().Queue()
    for f in filenames:
        p.apply_async(func=copy_file, args=(f, folder_path, new_folder_name, q,))

    done_num = 0.0
    all_num = len(filenames)
    while all_num > done_num:
        done_file = q.get()
        done_num += 1
        done_rate = done_num/all_num
        print "\r[Done] %s, 当前复制进度--%.2f%%" % (done_file, done_rate*100)

if __name__ == "__main__":
    main()
'''
#52. 单例模式
'''
class Test(object):

    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Test, cls).__new__(cls)
        return cls.instance

    init_flag = False
    def __init__(self):
        if self.init_flag:
            return
        self.init_flag = True
        print "执行__init()___"

t1 = Test()
print t1
t2 = Test()
print t2
'''

#53. 找出相等的数字
'''
source = [1, 3, 8, 9, 15, 12, 15, 3, 3, 9]

def find_2dup(source):
    sl = len(source)
    if sl < 2:
        return []
    result = {}
    for s in source:
        result[s] = result.get(s, 0) + 1
    return [k for k, v in result.items() if v == 2]

if __name__ == "__main__":
    print find_2dup(source)
'''

#54. 反转Dict中的key和value
d = {'a': 1, 'b': 2, 'c': 3}
def revert_dict(source):
    return dict([(v, k) for k, v in d.items()])

if __name__ == "__main__":
    print revert_dict(d)

