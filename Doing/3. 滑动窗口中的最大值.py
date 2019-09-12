# coding: utf-8

def maxSlidingWindow(nums, k):
	if not nums: return []
	window, res = [], []
	for i, x in enumerate(nums):
		print "i= %d, k= %d, windows= %s, res= %s" % (i, k, window, res)
		if i >= k and window[0] <= i - k:                       # 删除掉window范围左侧的值
			window.pop(0)
		while window and nums[window[-1]] <= x:     # window中的值小于刚刚进入窗口的值
			window.pop(-1)
		window.append(i)
		if i >= k - 1:                                                      # 遍历的位置>=窗口大小
			res.append(nums[window[0]])
	return res

li = [1, 3, -1, -3, 5, 6, 7]
print maxSlidingWindow(li, 3)