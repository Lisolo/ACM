# coding=utf-8

"""
给你两个正整数a,b,  输出它们公约数的个数。
"""

a = 24
b = 30
count = 0
number = min(a, b)
for x in xrange(1, number + 1):
    if a % x == 0 and b % x == 0:
        count += 1
print count

def common_divisor(number):
    divisor = []
    for x in xrange(1, number + 1):
        if number % x == 0:
            divisor.append(x)
    return divisor

list_a = common_divisor(a)
list_b = common_divisor(b)
list_c = list(set(list_a) & set(list_b))
print len(list_c)