# coding=utf-8

"""
给你一个十进制数a，将它转换成b进制数,如果b>10,用大写字母表示（10用A表示，等等）
a为32位整数，2 <= b <= 16
如a=3,b = 2, 则输出11
"""

a = 332
b = 16
c = []
d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def convert(number1, number2):
    if number1 > 0:
        while number1 > 0:
            c.append(d[number1 % number2])
            number1 /= number2
    elif number1 == 0:
        c.append('0')
    else:
        number1 = -number1
        while number1 > 0:
            c.append(d[number1 % number2])
            number1 /= number2
        c.append('-')
    return c[::-1]
print(''.join(convert(a, b)))

"""solution 2:"""
e = '0123456789ABCEDFGHIJKLMNOPQRSTUVWXYZ'
def f(x,y):
    s = []
    while x >= y:
        s.append(x % y)
        x /= y
    s.append(x)
    return ''.join([e[c] for c in s[::-1]])

print((a < 0 and '-' or '') + f(abs(a), b))