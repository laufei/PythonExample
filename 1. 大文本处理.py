# coding: utf-8

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