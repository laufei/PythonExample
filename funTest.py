# coding: utf-8
__author__ = 'liufei'

def caller_fun(f):
    f()

def testFun():
    print "I'm testFun~"

caller_fun(testFun)