# coding=utf-8

"""
小Py要吃西瓜，想知道切了n刀后，最多能切出多少块？请你们帮助下小Py.
给你一个正整数n（0 < n < 10^3),你输出一个数字，代表最多能切多少块。
如n=1, 输出2。
"""

n = 4
print '%.f' % (1.0 / 6 * (n**3 + 5*n + 6))