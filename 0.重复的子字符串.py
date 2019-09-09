# coding: utf-8

def repeatedSubstringPattern(s):
	slen = len(s)
	for i in range(slen//2):
		if slen % (i+1) == 0 and s[:i+1] * (slen//(i+1)) == s:
			return True
	return False

def repeatedSubstringPattern_1(s):
	return (s + s)[1: len(s)*2-1].find(s) != -1

def repeatedSubstringPattern_2(s):
	return (s + s)[1:len(s)*2-1].count(s) != 0

def repeatedSubstringPattern_3(s):
	return s in (s + s)[1: len(s)*2-1]

s = "abcabcabcabc"
print(repeatedSubstringPattern(s))
print(repeatedSubstringPattern_1(s))
print(repeatedSubstringPattern_2(s))
print(repeatedSubstringPattern_3(s))
