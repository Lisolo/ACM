# coding=utf-8

"""
给你一个仅有小写字母组成的字符串s（len(s) < 10)，请你输出s内的所有字母的全排列，每行输出一个，
按照字典序升序输出。
如：s="bbjd",则输出：
bbdj
bbjd
bdbj
bdjb
bjbd
bjdb
dbbj
dbjb
djbb
jbbd
jbdb
jdbb
"""

import itertools

s = 'bbjd'
list_a = itertools.permutations(s)
list_b = sorted(list(set(list_a)))
for x in list_b:
    print ''.join(x)