from math import gcd
n = int(input())
alist = list((map(int, input().split())))
ans = gcd(alist[0], alist[1])
for i in range(2, n):
    ans = gcd(ans, alist[i])
print(ans)