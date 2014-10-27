# coding=utf-8

"""
We can use loops to simulate natural processes over time. 
Write a program that calculates the populations of two kinds of “wumpuses” over time. 
At the beginning of year 1, there are 1000 slow wumpuses and 1 fast wumpus. 
This one fast wumpus is a new mutation. 
Not surprisingly, being fast gives it an advantage, as it can better escape from predators. 
Each year, each wumpus has one offspring. 
(We'll ignore the more realistic niceties of sexual reproduction, 
like distinguishing males and females.). There are no further mutations, 
so slow wumpuses beget slow wumpuses, and fast wumpuses beget fast wumpuses. 
Also, each year 40% of all slow wumpuses die each year, 
while only 30% of the fast wumpuses do.

So, at the beginning of year one there are 1000 slow wumpuses. 
Another 1000 slow wumpuses are born. 
But, 40% of these 2000 slow wumpuses die, 
leaving a total of 1200 at the end of year one. 
Meanwhile, in the same year, we begin with 1 fast wumpus, 
1 more is born, and 30% of these die, leaving 1.4. 
(We'll also allow fractional populations, for simplicity.) 

The anwser is 45
"""

class slow_wumpuses:
    def __init__(self):
        self.people = 1000
        
    def __str__(self):
        return str(self.people)
    
    def born(self):
        self.people *= 2
        
    def die(self):
        self.people *= 0.6
        
    def slow(self):
        return self.people
    
class fast_wumpuses:
    def __init__(self):
        self.people = 1
        
    def __str__(self):
        return str(self.people)
    
    def born(self):
        self.people *= 2
        
    def die(self):
        self.people *= 0.7 
        
    def fast(self):
        return self.people
        
slow = slow_wumpuses()
fast = fast_wumpuses()
for n in range(0, 100):
    if int(fast.fast()) > int(slow.slow()):
        print n
    slow.born()
    fast.born()
    slow.die()
    fast.die()
    print slow 
    print fast
    print ''