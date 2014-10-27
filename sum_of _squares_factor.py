# coding=utf-8

"""
6的因子有1, 2, 3 和 6, 它们的平方和是1 + 4 + 9 + 36 = 50. 如果f(N)代表正整数N所有因子的平方和, 那么f(6) = 50.
现在令F代表f的求和函数, 亦即F(N) = f(1) + f(2) + .. + f(N), 显然F一开始的6个值是: 1, 6, 16, 37, 63 和113.
那么对于任意给定的整数N(1 <= N <= 10^8), 输出F(N)的值.
"""

N = 6

def factors(number):
    list_factors = []
    for x in xrange(1,number+1):
        if number % x == 0:
            list_factors.append(x)
    return list_factors

def sum_of_squares(list_factors):
    result = 0
    for x in list_factors:
        result += x**2
    return result

def fn(n):
    result = 0
    for x in xrange(1,n+1):
        result += sum_of_squares(factors(x))
    return result
    
print fn(N)

"""solution 2:"""
def F(N):
    result = 0;
    for x in xrange( 1, N /2 + 1):
        result += ((N / x) * (x**2));
    result += ( N * ( N + 1) * (2 * N   + 1) - ( N/ 2 ) * ( N /2 + 1) * ( (N/2)* 2 + 1)) / 6;
    return result;

print F(N);