# coding=utf-8

"""
给你一个整数数列a1,a2,a3,...,an,请你修改（不能删除，只能修改）最少的数字，使得数列严格单调递增。
数列存储在列表L中，你可以直接使用L，L的长度小于100000。
注意：必须保证修改后的数列依然是整数序列，不能修改成小数。
例如：L=[1,3,2],则输出1
"""

L = [1, 3, 2]

def getSteps(my_list):
    length = len(my_list)
    if length < 1:
        return 0
    dp = [1] * length
    dp1 = [-1] * length
    for x in xrange(length-2, -1, -1):
        for y in xrange(length-1, x, -1):
            if (my_list[y]-my_list[x] >= y-x and dp[y]+1>dp[x]): 
                dp[x] = dp[y] + 1
                dp1[x] = y
    i = dp.index(max(dp))
    L[0:i] = range(my_list[i]-i, my_list[i])
    while(dp1[i] != -1):
        my_list[i + 1: dp1[i]] = range(my_list[i]+1, my_list[i]+dp1[i]-i)
        i = dp1[i];
    my_list[i + 1:] = range(my_list[i]+1, my_list[i]+length-i)
    return length - max(dp)

print getSteps(L)