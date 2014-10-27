# coding=utf-8

"""
给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
如：st="00:00:00", et="00:00:10", 则输出10.
"""

def time_difference(t1, t2):
    t1 = map(int, t1.split(':'))
    t2 = map(int, t2.split(':'))
    dif = 0
    for x, y in zip(t2, t1):
        dif = dif * 60 + (x - y)
    print dif

st = '00:00:00'
et = '23:59:59'
time_difference(st, et)