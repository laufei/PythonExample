# coding: utf-8

# @Time    : 2019/7/30 5:49 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 大文本处理.py
# @Software: PyCharm

# coding: utf-8

# @Time    : 2019/7/30 5:49 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 大文本处理.py
# @Software: PyCharm

def readInChunks(fileObj, chunkSize=4096):
		while True:
			line = fileObj.read(chunkSize)
			if not line:
				break
			else:
				yield line

def read():
	index = 0
	with open("bigFile", "rb") as f:
		for i in readInChunks(f):
			index += 1
			print "[%d]-%s" % (index, i)

read()