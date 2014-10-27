# coding=utf-8

"""
又是回文数！但这次有所不同了。
给定一个N进制正整数，把它的各位数字上数字倒过来排列组成一个新数，然后与原数相加，
如果是回文数则停止，如果不是，则重复这个操作，直到和为回文数为止。
如果N超过10，使用英文字母来表示那些大于9的数码。例如对16进制数来说，
用A表示10，用B表示11，用C表示12，用D表示13，用E表示14，用F表示15。
例如：10进制87则有：
STEP1: 87+78=165
STEP2: 165+561=726
STEP3: 726+627=1353
STEP4: 1353+3531=4884
给你一个正整数N(2<=N<=16)和字符串M（"1"<=M<="30000"(10进制)）,表示M是N进制数，输出最少经过几步可以得到回文数。
如果在30步以内（含30步）不可能得到回文数，则输出0。输入的数保证不为回文数。
如N=10, M="87", 则输出4.注意：M是以字符串的形式给定的。
"""

Numbers = "0123456789ABCDEF"

def getNumber10(M,base):
    return reduce(lambda x,y: x * base + Numbers.index(y), M, 0)

def getNumberAndReverseNmuber(M,base):
    strM = ""
    reverseStrM = ""
    intM = M
    reverseIntM = 0
    while M > 0:
        num = M % base; 
        char = Numbers[num]
        strM = char + strM
        reverseStrM += char
        reverseIntM = reverseIntM * base + num
        M = M / base

    return [strM,intM,reverseStrM,reverseIntM]

def getSteps(N, M):
    L = getNumberAndReverseNmuber(getNumber10(M, N), N)
    M = L[1] + L[3]
    steps = 0
    while steps ==0 or  (L[0] != L[2] and steps <= 30):
        M = L[1] + L[3]
        L = getNumberAndReverseNmuber(M, N)
        steps += 1
    if steps > 30:
        return 0
    return steps

print getSteps(N,M)