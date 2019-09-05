# coding: utf-8
__author__ = 'liufei'

'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''

def fn():
    score = raw_input("Please input your score:")
    if not score.isdigit():
        assert False, "Invalid input!"
    else:
        score = int(score)
    if score < 0 or score > 100:
        assert False, "Invalid input!"
    print "A" if score >= 90 else "B" if score >59 and score <90 else "C"

fn()
