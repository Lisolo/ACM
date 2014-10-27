# coding=utf-8

"""
现在我们手里有一张2维的正整数(包括0)表.
对于第i行第j列的那个数我们有如下定义：
a[i][j]是 a[i][k]{其中0<=k<j}和a[k][j]{其中0<=k<i}没有出现的那个最小的正整数
比如a[0][0]=0;
现在给你两个非负整数x,y,（0 <= x,y <= 10^9),请你输出a[x][y]的值。
如：x=0,y=0, 则输出0
    x=0,y=1, 则输出1
    x=1,y=0, 则输出1
    x=1,y=1, 则输出0
"""

def findValue(i, j):
    k = 1
    if i==0:
        return j
    if j==0:
        return i
    if i==j:
        return 0

    while 2*k-1<=max(i, j):
        k *= 2
    m = 0
    
    while k>1:
        if (i>=k and j<k) or (i<k and j>=k):
            m += k
        if i>=k:
            i -= k
        if j>=k:
            j -= k
        k /= 2
    return m + findValue(i, j)

print findValue(x, y)