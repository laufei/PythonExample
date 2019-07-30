# coding: utf-8

# @Time    : 2019/7/30 5:49 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 大文本处理.py
# @Software: PyCharm

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