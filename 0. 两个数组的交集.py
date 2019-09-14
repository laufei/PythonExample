# coding: utf-8
def intersect(nums1, nums2):
		inter = set(nums1) & set(nums2)
		l = []
		for i in inter:
			l += [i] * min(nums1.count(i), nums2.count(i))
		return l

nums1 = [1, 2, 2, 1, 3]
nums2 = [2, 2, 3, 3, 3]
print(intersect(nums1, nums2))