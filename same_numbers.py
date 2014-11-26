# coding=utf-8

"""
给你一个整数列表L, 判断L中是否存在相同的数字，
若存在，输出YES，否则输出NO。
"""

L = [1, 5, 3, 4]
flag = 0

for x in L:
    if L.count(x) >= 2:
    	flag = 1
    	break
if flag:
	print('YES')
else:
	print('NO')