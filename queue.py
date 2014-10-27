# coding=utf-8

"""
全班N（2<=N<=45）个人排成一排，但因为高矮不齐，需要进行调整。调整的方法是，不调换左右次序，只让若干人后退一步变为第2排，
使第一排留下的人从左到右的身高按降序排列，即右边的人不比左边的人高。如果第2排的人还不按降序排列，
则照此办理，即再让第2排的若干人后退一步变为第3排，这样继续下去，直到所有排的人都按身高从高到低排列。
现在将每个人的身高保存在列表L中，给你L，请你找出一种使第一排留下的人数尽可能多的调整方法，
输出第一排留下的人数P及最后调整完共有几排数K，P和K之间以一个空格隔开。
如，L=[130, 122, 112, 126, 126, 125, 120, 100],则输出6 2。
"""

L = [130, 122, 112, 126, 126, 125, 120, 100]
list_a = []
for x in xrange(0, len(L)-1):
	if L[x+1] >= L[x]:
		list_a.append(x+1)

list_b = list(set(L) - set(list_a))

def deal(L):
    path=[ [] for i in range(len(L)) ]
    location = [ [] for i in range(len(L)) ]
    flag = [-1 for i in range(len(L))]
    flag[0]=1
    path[0]=[L[0]]
    location[0]=[0]
    for j in range(1, len(L)):
        for k in range(0, j):
            if L[k]>=L[j] and flag[j]<flag[k]+1:
                flag[j] = flag[k] + 1
                path[j] = [item for item in path[k]]
                path[j].append(L[j])
                location[j]=[item for item in location[k]]
                location[j].append(j)
        if flag[j]==-1:
            flag[j] = 1
            path[j].append(L[j])
            location[j].append(j)
    idexoutL = 0
    maxoutL = len(location[0])
    for i in range(1, len(location)):
        if len(location[i])>maxoutL:
            maxoutL = len(location[i])
            idexoutL = i
    outL = location[idexoutL]
    return [L[i] for i in range(len(L)) if i not in outL], len(outL)

k = 1
tmp = 0
deal(L)
L, maxfirstnum = deal(L)
while(L!=[]):
    L, tmp = deal(L)
    k += 1
print maxfirstnum, k 