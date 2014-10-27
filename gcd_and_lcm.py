# coding=utf-8

"""
我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。
注：所给数据都有解，不用考虑无解的情况。
"""

import math

a = 4
b = 7
e = b /a
mid = int(math.sqrt(e))
c = [x for x in range(1, mid + 1) if e % x == 0]
d = reduce(lambda p, x: (x, e / x, x + e / x) if x + e / x < p else p, c, (0, 0, 0))
print "%d %d" % (a * d[0], a * d[1])