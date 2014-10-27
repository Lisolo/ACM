# coding=utf-8

"""
在RSA密码体系中,欧几里得算法是加密或解密运算的重要组成部分。它的基本运算过程就是解 (x*a) % n = 1 这种方程。
其中，x,a,n皆为正整数。现在给你a和n的值(1 < a,n < 140000000)，请你求出最小的满足方程的正整数解x（保证有解）.
如：a = 1001, n = 3837，则输出23。
"""

a = 1001
n = 3837
list_x = []

for x in xrange(1,10000000):
    if (x*a)%n == 1:
        list_x.append(x)

list_x.sort()
print list_x[0]