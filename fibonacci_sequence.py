# coding=utf-8

"""
斐波那契数列为1,1,2,3,5,8...。数列从第三项起满足，该项的数是其前面两个数之和。
现在给你一个正整数n（n < 10000), 请你求出第n个斐波那契数取模20132013的值（斐波那契数列的编号从1开始）。
"""

n = 10
fibonacci_sequence = [1, 1]

def fibonacci(i):
    b = fibonacci_sequence[i-1] + fibonacci_sequence[i]
    fibonacci_sequence.append(b)

for x in xrange(1,n-1):
    fibonacci(x)

print fibonacci_sequence[n-1] % 20132013