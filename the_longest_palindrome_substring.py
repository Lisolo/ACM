# coding=utf-8

"""
记得一副有趣的对联: "雾锁山头山锁雾, 天连水尾水连天", 上联和下联都是回文的.
当然类似的还有: "上海自来水水来自海上, 山西悬空寺寺空悬西山".
回文是什么意思? 就是把内容反过来读也是和原来一样的, 譬如abccba, xyzyx, 这些都是回文的.
然而我们更感兴趣的是在一个英文字符串L中, 怎么找出最长的回文子串.
例如L = "caayyhheehhbbbhhjhhyyaac", 那么它最长的回文子串是"hhbbbhh".
这个任务看似简单, 但是如果我告诉你L的长度可能会接近10^4, 问题似乎就变麻烦了.
不管怎么说, 加油吧骚年.
"""

L = 'caayyhheehhbbbhhjhhyyaac'
m, n = 0, 0

for i in range(len(L)):
    for j in range(i+1-(n-m)):
        if L[j:i+1] == L[j:i+1][::-1]:
            m, n = j, i+1
            break

print L[m:n]

L = '#'.join(list(L)) 
length = len(L)

q, r = 0, 0 
for i in range(1,length):
    if i+r < length and L[i-r:i] == L[i+r:i:-1]:
        q, r = i, r
        while i+r+1<length and L[i-r-1] == L[i+r+1]:
            r += 1

L1 = L[q-r:q+r+1]
t1, t2 = L1[::2], L1[1::2]
print t1 if any(i != '#' for i in t1) else t2