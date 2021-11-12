n = int(input())
l = [int(input()) for i in range(n)]
dp = [0]*10001
dp[0] = 1
for i in range(n):
    for j in reversed(range(10001)):
        if dp[j] == 0: continue
        if j + l[i] <= 10000:
            dp[j + l[i]] = 1
ans = 0
for i in range(10001):
    if dp[i] == 1 and i % 10: ans = max(ans, i)
print(ans)