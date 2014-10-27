# coding=utf-8

"""
Give you a positive integer list L, such as L=[2,8,3,50], print out the 0 at the end of the product of all number in L.
"""

L = [2, 8, 3, 50]
result = 1

for x in L:
    result *= x

b = str(result)
c = 0

for x in b:
    if x == '0':
        c += 1

print c

count_2 = 0
count_5 = 0

for x in L:
    while x % 2 == 0:
        x /= 2
        count_2 += 1
    while x % 5 == 0:
        x /= 5
        count_5 += 1

print min(count_2, count_5)