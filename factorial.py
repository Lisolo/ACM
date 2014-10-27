# coding=utf-8

"""
N的阶乘定义为：N!=N×(N－1)×……×2×1
请编写一个程序，输出N的阶乘的十进制表示中从最末一个非0位开始自低位向高位数的第K位。
现在给你N和K（0<=N<=10000，1<=K<=5），请你输出要求的数字(保证存在）。
例如：N=5,K=2,则输出1   note:（5!=120);
     N=8,K=3,结果为0   note:（8!=40320）
"""

N = 5
K = 2

def factorial(number):
    return reduce(lambda x, y: x * y, xrange(1, number+1))

a = str(factorial(N))
a = a[::-1]
for x in xrange(0, len(a)-1):
    if a[x] == '0':
        print a[x+K]
        break