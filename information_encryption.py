# coding=utf-8

"""
给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。
这里将字母表的z和a相连，如果超过了z就回到了a。例如a="cagy",b=3, 则输出 fdjb
"""

a = 'abhfgfd'
b = 12

def encrypt(s, number):
    c = []
    d = []
    e = []
    for x in s:
        c.append(ord(x) + number)

    for x in c:
        if x > 122:
            x = x % 122 + 96
            d.append(x)
        else:
            d.append(x)

    for x in d:
        e.append(chr(x))
    return e

print ''.join(encrypt(a, b))

def jiami(a,b):
    L = []
    b = b%26
    for aa in a :
        if b > (122-ord(aa)):
            z = chr((ord('a')-1)+(b - (122-ord(aa))))
            L.append(z)
        else:
            z = chr((ord(aa)+b))
            L.append(z)
    return L

print ''.join(jiami(a,b))
#mntrsrp