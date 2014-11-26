# coding=utf-8

"""
Give you an integer a, print out the number 1 in binary  a.
"""

a = 12
bin_a = list(bin(a))

number = bin_a.count('1')

print(number)