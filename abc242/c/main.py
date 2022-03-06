n = int(input())
mod = 998244353
# 表を作る
dp = [[0]*10 for _ in range(n+1)]
# 一桁かつ末尾が1である数字を埋める
for i in range(1,10):
    dp[1][i] = 1
# 二桁からn桁まで埋める
for i in range(2, n+1):
    for j in range(1,10):
        # 末尾が1なら上と右上の値を使う
        if j == 1:
            dp[i][j]=dp[i-1][j]+dp[i-1][j+1]
        # 末尾が1と9以外なら左上と上と右上の値を使う
        if 2 <= j <= 8:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+dp[i-1][j+1]
        # 末尾が9なら左上と上の値を使う
        if j == 9:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        # あまり
        dp[i][j] %= mod
print(sum(dp[n])%mod)