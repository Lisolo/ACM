# coding=utf-8

import datetime

year = '2014'

def isLeapYear(y):
    y = int(y)
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print 366
    else:
        print 365

def isLeapYear2(y):
    y = int(y)
    y1 = datetime.datetime(y, 1, 1)
    y2 = datetime.datetime(y+1, 1, 1)
    print str(y2 - y1).split(' ')[0]

isLeapYear(year)
isLeapYear2(year)   