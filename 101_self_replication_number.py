# coding=utf-8

"""
什么叫自复制数呢？我们看看下面的例子：
625×625=390625
376×376=141376
9376×9376=87909376
90625×90625=8212890625
如果一个数的平方末尾还是这个数本身，那么它就是自复制数。
现在告诉你长度为101位的自复制数只有一个，你能把它找出来吗？请输出这个101位的自复制数。
"""

a = 376

def getTail(n):
    i = 1
    c = n % (10 ** i)
    while not c:
        i += 1
        c = n % (10 ** i)
    return 10 ** (len(str(c))) - c

for i in range(100):
    ta = len(str(a))
    asquare = a ** 2
    b = asquare % (10 ** ta) + getTail(asquare / (10 ** ta)) * (10 ** ta)
    if len(str(b)) == 101:
        print(b)
        break
    a = b