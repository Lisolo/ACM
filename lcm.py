# coding=utf-8

"""
给你一个正整数list L, 如 L=[2,8,3,50], 求列表中所有数的最小公倍数(不用考虑溢出问题）。
如L=[3,5,10], 则输出30
"""

from functools import reduce

L = [2, 8, 3, 50]

def gcd(c, d):
    while (c % d != 0):
        e = c % d
        c = d
        d = e
    else:
        return d

def lcm(f, g):
    return (f * g / gcd(f, g))

print reduce(lambda x, y: lcm(x, y), L)