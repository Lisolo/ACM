# coding=utf-8

"""
给你两个正整数a,b,  输出它们公约数的个数。
"""

a = 24
b = 30

list_a = [x for x in range(1, a+1) if a % x == 0]
list_b = [x for x in range(1, b+1) if b % x == 0]
list_c = set(list_a) & set(list_b)
print(len(list_c))