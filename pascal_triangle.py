# coding=utf-8


"""
还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
..............
先在给你一个正整数n，请你输出杨辉三角的前n层
注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。
如n=2,则输出：
1
1 1
"""


n = 6
list1 = [1, 1]
list2 = [[1], [1, 1]]


print 1
print 1, 1


for x in xrange(2, n):
	list3 = [1]
	for y in xrange(1, len(list1)):
		list3.append(list1[y-1]+list1[y])
	list3.append(1)
	list1 = list3
	print ' '.join(str(x) for x in list1)
	list2.append(list1)


for x in list2:
    print ' '.join(str(y) for y in x)
