# coding=utf-8

"""
给你一个整数列表L,判断L中是否存在相同的数字，
若存在，输出YES，否则输出NO。
"""

L = [1, 5, 1, 3, 4]
a = 0

for x in L:
    if a <= L.count(x):
        a = L.count(x)

if a >= 2:
    print 'YES'
else:
    print 'NO'
