# coding=utf-8

"""
给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
若是锐角三角形，输出R,
若是直角三角形，输出Z，
若是钝角三角形，输出D，
若三边长不能构成三角形，输出W.
"""

a = 12
b = 13
c = 15
d = []

def is_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return 1
    else:
        return 0

def shape_of_triangle(side1, side2, side3):
    d.append(side1)
    d.append(side2)
    d.append(side3)
    d.sort()
    if is_triangle(side1, side2, side3):
        if d[2]**2 < d[0]**2 + d[1]**2:
            print 'R'
        elif d[2]**2 == d[0]**2 + d[1]**2:
            print 'Z'
        else:
            print 'D'
    else:
        print 'W'

shape_of_triangle(a, b, c)