# coding=utf-8

"""
给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。
若能，输出YES，否则输出NO。
"""

a = 12
b = 13
c = 15

def is_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print 'YES'
    else:
        print 'NO'

is_triangle(a, b, c)