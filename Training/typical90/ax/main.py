n,l = map(int, input().split())
# 段数の配列
dp = [0]*(n+1)
MOD = 1000000007
dp[0] = 1
# 1段ごとに到達可能か見ていく
for i in range(1,n+1):
    # 1段ごとの通り数
    if i < l:
        dp[i] = dp[i-1]
    # lからの通り数
    else:
        # 1段で到達する通り数とl段で到達する通り数
        dp[i] = (dp[i-1] + dp[i-l])%MOD
print(dp[n])

