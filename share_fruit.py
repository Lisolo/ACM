# coding=utf-8

"""
桌子上有一堆数量不超过20的果子，每个果子的重量都是不超过20的正整数，全部记录在列表 L 里面。
小明和小红决定平分它们，但是由于他们都太自私，没有人愿意对方比自己分得的总重量更多。
而果子又不能切开，所以最后他们商量好的平分方案是这样的：
他们可以把某些果子扔掉，再将剩下的果子平分，那么请问这种方案下他们每人最多可以分得多少重量的果子呢？
举个例子，如果 L = [1,2,3,4,5]，那么他们最好的方案是把重量为 1 的果子扔掉，一人分得总重量为 7 的果子；
相反，如果 L = [1,3,6], 那么他们一人分得的果子重量就是 0。
"""

import itertools

L = [1,3,6]
ok = set(sum(j) for i in xrange(2, len(L)+1) \
	for j in itertools.combinations(L,i)) \
    & set(2*sum(j) for i in xrange(1, len(L)/2+1) \
    for j in itertools.combinations(L,i))
print max(ok)/2 if ok else 0