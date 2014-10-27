# coding=utf-8

"""
给你一个整数组成的列表L，按照下列条件输出：
若L是升序排列的,则输出"UP";
若L是降序排列的,则输出"DOWN";
若L无序，则输出"WRONG"。
"""

L = [1, 1, 1, 1, 1]
flag1 = 0
flag2 = 0

for x in xrange(0, len(L)-1):
    if L[x] <= L[x+1]:
        flag1 += 1
    elif L[x] > L[x+1]:
        flag2 += 1

if flag1 == len(L)-1:
    print 'UP'
elif flag2 == len(L)-1:
    print 'DOWN'
else:
    print 'WRONG'
print L == sorted(L) and 'UP' or L == (sorted(L)[::-1]) and 'DOWN' or 'WRONG'