# coding: utf-8

# 二数之和
def two_sum_2(li, target):
	llen = len(li)
	dic = {}
	for i in range(llen):
		a = li[i]
		b = target - a
		if b not in dic:
			dic[a] = i
		else:
			return dic[b], i
if __name__ == "__main__":
	li = [1, 4, 8, 9, 5, 2]
	print two_sum_2(li, 13)

# 三数之和
def three_sum_2(li, targe):
	llen = len(li)
	if llen < 3:
		raise Exception, "列表长度不符合要求!"
	for i in range(llen-1):
		dic = {}
		for j in range(i+1, llen):
			a = li[i]
			b = li[j]
			c = targe - a - b
			if c not in dic:
				dic[a] = i
				dic[b] = j
			else:
				return i, dic[c], j
if __name__ == "__main__":
	li = [7, 5, 1, 9]
	print three_sum_2(li, 17)

# 三数之和等于0
def three_sum_0(li):
	llen = len(li)
	res = set()
	if llen < 3:
		raise Exception, "列表长度不符合要求!"
	li.sort()
	for i in range(llen-1):
		dic = {}
		for j in range(i+1, llen):
			c = -li[i]-li[j]
			if c not in dic:
				dic[li[i]] = 0
				dic[li[j]] = 0
			else:
				res.add((li[i], c, li[j]))
	return map(list, res)

if __name__ == "__main__":
	li = [-1, 0, 1, 2, -1, -4]
	print three_sum_0(li)


