# coding: utf-8

def longestConsecutive(nums):
	if len(nums) < 2:
		return len(nums)
	begin = 0
	count = 1
	maxc = 1
	for i in range(1, len(nums)):
		if nums[i - 1] + 1 == nums[i]:
			count += 1
			maxc = max(count, maxc)
			begin = i - maxc + 1
		else:
			count = 1
	return nums[begin: begin + maxc]

if __name__ == "__main__":
	l = [21,22,23,1,2,3,4,6,5]
	print (longestConsecutive(l))