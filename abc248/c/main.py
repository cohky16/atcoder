import math
n,m,k = map(int, input().split())
ans = 0
for i in range(m,k):
    ans += math.factorial(i)%998244353
print(ans%998244353)