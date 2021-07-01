# Given an array, rotate the array to the right by k steps, where k is non-negative.


import math


def rotate(nums, k):
	if k == 0:
		return
	n = len(nums)
	d = math.gcd(k, n)
	for i in range(d):
		temp = nums[i]
		for j in range(n // d):
			temp, nums[((j + 1) * k + i) % n] = nums[((j + 1) * k + i) % n], temp
