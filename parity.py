# coding=utf-8

"""
给你一个正整数列表 L, 如 L=[2,8,3,50], 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
奇数输出1,偶数输出0. 如样例输出应为0
"""

L = [2, 8, 3, 50]
result = 1
for x in L:
    result *= x

while result % 10 == 0:
     result /= 10
print result % 10 % 2
count_2 = 0
count_5 = 0
for x in L:
    while x % 2 == 0:
        x /= 2
        count_2 += 1
    while x % 5 == 0:
        x /= 5
        count_5 += 1
if count_2 > count_5:
    print 0
else:
    print 1