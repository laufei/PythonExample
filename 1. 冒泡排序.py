# coding: utf-8

def bubbleSort(arr):
	n = len(arr)

	for i in range(n):
		for j in range(n-i-1):
			print arr
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr
arr = [64, 34, 25, 12, 22, 11, 90, 20]

print(bubbleSort(arr))

