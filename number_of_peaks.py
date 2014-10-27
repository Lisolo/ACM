# coding=utf-8

"""
十一假期,小P出去爬山,爬山的过程中每隔10米他都会记录当前点的海拔高度(以一个浮点数表示),
这些值序列保存在一个由浮点数组成的列表h中。回到家中，小P想研究一下自己经过了几个山峰，请你帮他计算一下，输出结果。
例如：h=[0.9,1.2,1.22,1.1,1.6,0.99], 将这些高度顺序连线，会发现有两个山峰，故输出一个2(序列两端不算山峰)
"""

h = [0.9, 1.2, 1.22, 1.1, 1.6, 0.99]
peaks = []
count = 0

for x in xrange(len(h)-1):
	if h[x+1] >= h[x]:
		peaks.append('+')
	else:
		peaks.append('-')

for x in xrange(1, len(h)-1):
	if h[x-1] < h[x] and h[x] > h[x+1]:
		count += 1
print count