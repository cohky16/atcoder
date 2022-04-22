MOD = 998244353
N, M, K = map(int, input().split())
# 数列のi番目まで決めて、総和がjである数
# e.g.) n = 2, k = 4 
# 1 0 0 0 0 -> (0,0)は1　初期値
# 0 1 1 1 0 -> (1,1~M)までの総和はそれぞれ1
# 0 0 1 2 3 -> 答え(総和2は1,総和3は2,総和4は3)
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K):
        # 1からMまで回す
        for k in range(1, M + 1):
            # 合計値が超えたら抜ける
            if j + k > K:
                break
            # 配るDP
            dp[i + 1][j + k] += dp[i][j]
            dp[i + 1][j + k] %= MOD
print(sum(dp[-1]) % MOD)
