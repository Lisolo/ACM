"""
1.Initialize n to be 1000. Initialize numbers to be a list of numbers from 2 to n, but not including n.
2.With results starting as the empty list, repeat the following as long as numbers contains any numbers.
    Add the first number in numbers to the end of results.
    Remove every number in numbers that is evenly divisible by (has no remainder when divided by) the number that you had just added to    results.
How long is results? 
"""

locals()["n"] = 1000
numbers = xrange(2, n)
locals()["results"] = []

while numbers != []:
    results.append(numbers[0])
    numbers = [n for n in numbers if n % numbers[0] != 0]
print len(results)

"""solution 2:"""
while len(numbers) != 0:
    results.append(numbers[0])
    for i in numbers:
        if i % results[-1] == 0:
           numbers.remove(i)           
print len(results)