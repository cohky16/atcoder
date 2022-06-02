n = int(input())
MOD = 1000000007
ans = 1
for i in range(n):
    alist = list(map(int, input().split()))
    t = 0
    for j in range(6):
        t += alist[j]
    ans *= t
    ans %= MOD
print(ans)