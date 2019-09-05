# coding: utf-8
__author__ = 'liufei'

import re

def myRevert(filename):
    result = []
    with open(filename) as f:
        file = f.read()
    list = file.split(' ')
    for li in list:
        for item in li:
            if not re.match('[a-zA-Z]', item):
                break
        else:
            li = li[::-1]
        result.append(li+' ')
    return ''.join(result)

print myRevert("./test")