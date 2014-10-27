# coding=utf-8

"""
给你两个整数a和b（-10000<a,b<10000），请你判断是否存在两个整数，他们的和为a，乘积为b。
若存在，输出Yes,否则输出No
例如：a=9,b=15, 此时不存在两个整数满足上述条件，所以应该输出No。
"""

a = 6
b = 9
divisors = []
flag = 0

if b >= 0:
    for x in xrange(-b, b+1):
        if x == 0: 
            pass
        else:
            b % x == 0
            divisors.append([x, b/x])
else:
    for x in xrange(b,-(b-1)):
        if x == 0: 
            pass
        else:
            b % x == 0
            divisors.append([x, b/x])

for x in divisors:
    if sum(x) == a:
        flag = 1

if a == 0 and b == 0:
    print 'YES'
else:    
    if flag:
        print 'YES'
    else:
        print 'NO'

"""solution 2:"""
delta = a**2 - 4 * b
if delta >= 0 and int(delta**0.5) == delta**0.5:
    print 'YES'
else:
    print 'NO'