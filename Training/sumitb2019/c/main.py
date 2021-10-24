x = int(input())
dp = [False]*101010
dp[0] = True
for i in range(x):
    if dp[i]:
        for j in range(6):
            dp[i + j + 100] = True
print("1") if dp[x] else print("0")

