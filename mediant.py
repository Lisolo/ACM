# coding=utf-8

"""
给你一个list L, 如 L=[0,1,2,3,4], 输出L的中位数（若结果为小数，则保留一位小数）。
"""

L = [0, 1, 2, 3, 4]
L.sort()
length = len(L)


if length % 2 == 0:
	index = length / 2
	print float(L[index] + L[index - 1]) / 2
else:
	print L[length / 2]
