# coding: utf-8

def merge(l1, l2):
	i1, i2 = 0, 0
	l = []
	try:
		while i1 < len(l1) and i2 < len(l2):
			if l1[i1] < l2[i2]:
				l.append(l1[i1])
				i1 += 1
			else:
				l.append(l2[i2])
				i2 += 1
		print l
		if i1 < len(l1):
			l.extend(l1[i1:])
		if i2 < len(l2):
			l.extend(l2[i2:])
	except:
		print('不能比较')
		return None
	return l

print(merge([1, 3, 3, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7], [2, 4, 4, 6, 7, 7, 7, 7, 7]))