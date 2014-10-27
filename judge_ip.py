# coding=utf-8

"""
互联网上的每台计算机都有一个IP，合法的IP格式为：A.B.C.D。
其中A、B、C、D均为位于[0, 255]中的整数。为了简单起见，我们规定这四个整数中不允许有前导零存在，如001这种情况。
现在给你一个字符串s(s不含空白符),请你判断s是不是合法IP，若是，输出Yes,否则输出No.
如：s="202.115.32.24", 则输出Yes;  
    s="a.11.11.11", 则输出No.
"""

import re

s = '202.115.32.24'
flag = 1

try:
    list1 = map(int, s.split('.'))
    if len(list1) > 4:
        flag = 0
    else:
        for x in list1:
            if x >= 0 and x <= 255: 
                pass
            else:
                flag = 0
except Exception, e:
    flag = 0

if flag == 1:
    print 'Yes'
else:
    print 'No'
print re.match(r'((2[0-4]\d?|25[0-5]|1\d{2}|[1-9]\d|\d)\.){3}(2[0-4]\d?|25[0-5]|1\d{2}|[1-9]\d|\d)$', s) and 'Yes' or 'No'