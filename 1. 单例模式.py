# coding: utf-8

# @Time    : 2019/8/25 8:28 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 单例模式.py
# @Software: PyCharm

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