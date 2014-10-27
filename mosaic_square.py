# coding=utf-8

"""
现在有一堆木棒，告诉你它们的长度，判断能否用这些木棒拼接成正方形。
注意：所有的木棒都要用上，且不能截断。
给你一个正整数list L, 如 L=[1,1,1,1], L中的每个数字代表一个木棒的长度，如果这些
木棒能够拼成一个正方形，输出Yes，否则输出No。
如L=[1,1,1,1]，则输出Yes;L=[1,1,1],则输出No。
注：数据已于2014-03-11加强，之前通过的代码可能无法再次通过
"""

L = [1, 1, 1, 1]

def canDivide(L, n):
    end, (div, mod) = len(L), divmod(sum(L), n)
    

    return end >= n and mod == 0 and canDivideBase(sorted(L, None,None,True),
                0, 0, end, div, div, n)

def canDivideBase(L, start, i, end, dividedSum, remain, n):
    for j in xrange(i, end):
        if L[j] == 0 or L[j] > remain: continue
        tmp, remain, L[j] = L[j], remain - L[j], 0
        if remain == 0:
            return n <= 2 \
                or canDivideBase(L, 0, 0, end, dividedSum, dividedSum, n-1)
        if canDivideBase(L, j+1, j+1, end, dividedSum, remain, n):
            return True
        if j == start: return False
        remain, L[j] = remain + tmp , tmp
    return False

print 'Yes' if canDivide(L, 4) else 'No'