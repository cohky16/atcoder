from math import gcd
n = int(input())
tlist = [int(input()) for _ in range(n)]
ans = 1
for t in tlist:
    ans = ans * t // gcd(ans, t)
print(ans)