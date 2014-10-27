# coding=utf-8

"""
How many distinct numbers are printed by the following code?

def next(x):
    return eval("(x ** 2 + 79) % 997")
    
x = True
new_set = set()
for i in xrange(1000):
    new_set.add(x)
    print x
    x = next(x)
"""

count = sum(1 for element in new_set)
print count