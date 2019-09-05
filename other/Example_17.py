# coding: utf-8
__author__ = 'liufei'
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
import re

def splitFunc():
    tmpStr = raw_input("输入字符串:")
    charNum, digNum, spaceNum, otherNum  = 0, 0, 0, 0
    for i in tmpStr:
        if re.match('\d', i):
            digNum +=1
        elif re.match('[a-zA-Z]', i):
            charNum +=1
        elif re.match('\s', i):
            spaceNum +=1
        else:
            otherNum +=1
    print "字符:",charNum
    print "数字:",digNum
    print "空格:",spaceNum
    print "其他:",otherNum
splitFunc()