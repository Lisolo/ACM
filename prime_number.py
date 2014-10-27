# coding=utf-8


"""
输出100以内的所有素数，素数之间以一个空格区分
"""


import math


N = 100
prime_list = []


for x in xrange(2,N):
    flag = 1
    for y in xrange(2,int(math.sqrt(x)) + 1):
        if x % y == 0:
            flag = 0
    if flag == 1:
        prime_list.append(x)


print ' '.join(str(x) for x in prime_list)



prime_list2 = [2]


for x in range(3,N+1):
    if all(x%y for y in prime_list2):
        prime_list2.append(x)
if N==1:
    print 0
else:
    print len(prime_list2)