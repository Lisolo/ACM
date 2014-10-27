# coding=utf-8

"""
把一个偶数拆成两个不同素数的和，有几种拆法呢？
现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
计算将该数拆成两个不同的素数之和的方法数，并输出。
如n=10，可以拆成3+7，只有这一种方法，因此输出1.
"""

import math

n = 10
count = 0
prime_list = []
for x in xrange(2,n):
    flag1 = 1
    for y in xrange(2,int(math.sqrt(x)) + 1):
        if x % y == 0:
            flag1 = 0
    if flag1 == 1:
        prime_list.append([x,n-x])
print prime_list

for my_list in prime_list:
    flag2 = 1
    if my_list[0] == my_list[1]: pass
    else:
        for y in xrange(2,int(math.sqrt(my_list[1])) + 1):
            if my_list[1] % y == 0:
                flag2 = 0
        if flag2 == 1:
            count += 1
print count / 2