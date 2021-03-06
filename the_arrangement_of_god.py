# coding=utf-8

"""
记得有一次全班去唱K, 其中有个活动是情歌对唱. 具体操作流程是这样的:
准备好 21 个阄(我们班 15 男 6 女), 其中只有两个是有标记的, 每人随意抓取一个, 最后取到有标记的阄的两个人去点首情歌对唱.
旁边一哥们儿幽幽地对我说, 看来搅基真是神的安排啊, 你看我们班的男女人数, 搅基的几率 C(15,2)/C(21,2) 刚好是 1/2.
给跪了, 这哥们儿对数字太敏感了, 简直是拉马努金转世啊. 不过我随之想到一个问题: (21, 15) 真的是神的唯一安排吗? 其实不是的,
神还有很多类似的安排. 比如 (4, 3), 显然 C(4,2)/C(3,2) 也等于 1/2, 当然还有 (120, 85) 等等等等.
神的安排太多太多了, 如果我们定义 (n, m) 是一个安排(其中 1 < m < n), 而如果 C(m,2)/C(n,2) = 1/2, 它就是神的安排.
现在的问题是, 给你一个不大于 10^9 的正整数 N, 有多少组神的安排 (n, m) 满足 n <= N 呢?
"""

N = 100
count1 = 0

def factorial(n):
    return reduce(lambda x, y: x * y, xrange(1, n+1)) * 1.0

def combination(n):
    return factorial(n) / (factorial(n-2) * factorial(2))

for x in xrange(3, N+1):
    for y in xrange(3, N+1):
        if combination(x) / combination(y) == 0.5:
            count1 += 1
print count1

count2 = 0
x, y = 1, 1
while x <= 2*N-1:
    x, y = 3 * x + 4 * y, 2 * x + 3 * y
    if x > 2*N-1:
        break
    if x%2 and y%2:
        count2 += 1
print count2