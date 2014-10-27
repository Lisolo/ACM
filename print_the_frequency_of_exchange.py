# coding=utf-8

"""
给你一个list L, 如 L=[2,8,3,50], 对L进行选择排序并输出交换次数,
如样例L的结果为1
"""

L = [2,8,3,50]

def sorting(my_list):
    length = len(my_list)
    count = 0
    for x in range(length):
        temp = 0
        for y in range(len(my_list[x:])):
            if my_list[x:][y] < my_list[x:][temp]:
                temp = y
        mini = temp
        if mini != 0:
            my_list[x], my_list[mini+x] = my_list[mini+x], my_list[x]
            count += 1
    return count

print sorting(L)