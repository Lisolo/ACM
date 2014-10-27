# coding=utf-8


"""
给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".
"""


a = 'wedabcdedcba'
n = 5


def find(s, number):
    flag = 0
    for x in xrange(len(s)-number+1):
        c = s[x:x+number]
        if c == c[::-1]:
            print 'YES'
            flag = 1
            break


    if flag == 0:
        print 'NO'


find(a, n)
