# coding=utf-8

"""
转换规则：如果数字d是x的约数，则x可以被转换为x+d。
现在给你两个正整数a和b，请你计算最少需要多少步能够将a转换成b。如果不能转换，则输出-1.
如：a = 1， b = 6, 则输出3.（1→2→4→6 或 1→2→3→6）
"""

a = 1
b = 9
count = 0
flag = 0

def divisor(number):
    list_divisor = [0]
    for x in xrange(1,number+1):
        if number % x == 0:
            list_divisor.append(x)
    return list_divisor

while a < b:
    for x in xrange(1,len(divisor(a))):
        if a + divisor(a)[-x] <= b:
            flag = x
            break
        else:
            flag = 0
    if flag == 0:
        pass
    else:
        a += divisor(a)[-flag]
        count += 1

print count