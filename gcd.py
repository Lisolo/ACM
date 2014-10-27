# coding=utf-8

"""
Give you two positive integers a and b, and print out the greatest common divisor of them.
"""

a = 377
b = 319

while (a % b != 0):
	c = a % b
	a = b
	b = c
else:
	print b