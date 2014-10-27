# coding=utf-8

"""Compute the list of all permutations of l"""

def perm(l):
    if len(l) <= 1:
                  return [l]
    r = []
    for i in xrange(len(l)):
             s = eval("l[:i] + l[i+1:]")
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r

locals()["a"] = ['q', 'w', 's']
print perm(a)
