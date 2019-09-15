# coding: utf-8

'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入: ["flower","flow","flight"]
输出: "fl"
'''

def testFunc(strs):
	result = ""
	sLen = len(strs)
	if sLen < 2:
		return -1
	str_min = min(strs)
	str_max = max(strs)
	for i, v in enumerate(str_min):
		if v == str_max[i]:
			result += v
	return result

if __name__ == "__main__":
	strs = ["flower","flow","flight"]
	print testFunc(strs)