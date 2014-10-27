# coding=utf-8

"""
有一组砝码，重量互不相等，分别为m1、m2、m3……mn；每种砝码的数量有无限个。 
现要用这些砝码去称物体的重量,给你一个重量n,请你判断有给定的砝码能否称出重量n。 
现在给你一个正整数列表w和一个正整数n，列表w中的第i个元素w[i]表示第i种砝码的重量，
n表示要你判断的重量。如果给定砝码能称出重量n，输出Yes，否则输出No。
例如，w=[2,5,11], n=9,则输出Yes（取两个2，一个5）。
"""

w = [2, 11, 5]
n = 9
result1 = 0
result2 = [0]

w.sort()
while result < n:
    for x in w:
        if (result + x) <= n:
            result += x

for x in xrange(1, n+1):
    for y in result2[::-1]:
        if x-y in w:
            result2.append(x)
            break
print 'Yes' if result2[-1] == n else 'No'