# coding=utf-8

"""
给你直角三角形的两个直角边的边长a,b,请你求出其斜边边长，结果保留小数点后三位小数。
如a=3, b =4, 则输出5.000。
"""

import math

a = 3
b = 4

def pythagorean_theorem(side1, side2):
    print '%.2f' % math.sqrt(side1**2 + side2**2)

pythagorean_theorem(a, b)