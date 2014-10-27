# coding=utf-8

"""
下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。
"""

n = 1
m = 2
steps = []
flag = 0

for i in xrange(-1, max(m/2,n)+1):
    for j in xrange(-1, max(m,n/2)+1):
        for k in xrange(-1, 2):
            for l in xrange(-1, 2):
                a1, a2, a3, a4 = i, j, k, l
                if m == 1:
                    a1, a4 = 0, 0
                if n == 1:
                    a2, a3 = 0, 0
                if 2*a1+a2-a3-2*a4 == m and a1+2*a2+2*a3+a4 == n and a1+a2 > 0:
                    steps.append(abs(a1)+abs(a2)+abs(a3)+abs(a4))
                    flag = 1

if flag:
    steps.sort()
    print steps[0]
else:
    print '-1'