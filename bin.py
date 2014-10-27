# coding=utf-8

"""
Give you an integer a, print out the number 1 of a in the binary representation.
"""

count = 0
a = 12
bin_a = list(bin(a))

for x in bin_a:
	if x == '1':
	    count += 1
print count
