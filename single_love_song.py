# coding=utf-8

"""
抓不住爱情的我 
总是眼睁睁看它溜走 
...

现在来练习一下发现爱的能力，给你一个字符串a,如果其中包含"LOVE"（love不区分大小写)则输出LOVE，否则输出SINGLE。
"""

a = 'abcSinGlelove'

def find_love(b):
	lower_b = b.lower()
	if 'love' in lower_b:
		print 'LOVE'
	else:
		print 'SINGLE'

find_love(a)