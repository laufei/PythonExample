# coding: utf-8

def isIsomorphic(s, t):
	s = [s.index(i) for i in s]
	t = [t.index(i) for i in t]
	print s, t
	return s == t

s1, t1 = "egg", "add"
s2, t2 = "foo", "bar"
s3, t3 = "paper", "title"
print(isIsomorphic(s1,t1))
print(isIsomorphic(s2,t2))
print(isIsomorphic(s3,t3))
