# coding: utf-8
__author__ = 'liufei'
'''
题目：打印出如下图案（菱形）:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
from sys import stdout

def fn(x):
    for i in range((x-1)/2+1):
        for j in range((x-1)/2-i):
            stdout.write(' ')
        for k in range(2*i+1):
            stdout.write('*')
        print

    for i in range((x-1)/2):
        for k in range(i+1):
            stdout.write(' ')
        for j in range(x-2*i-2):
            stdout.write('*')
        print

fn(int(raw_input("请输入一个奇数:")))

