n = int(input())
a = list(map(int,input().split()))
t = sum(a)
ans = 2020202021
lft = 0
for i in range(n):
    ans = min(ans, abs(t - (lft * 2)))
    lft += a[i]
print(ans)
