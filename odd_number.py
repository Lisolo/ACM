# coding=utf-8

"""
Give you a string a, then print out the character of odd position. For example a= '12345', then print out 135.
"""

a = '12345'

b = a[::-2]
print int(b[::-1])
print a[::2]