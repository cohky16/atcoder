s = input()
MOD = 1000000007
dp=[[0 for _ in range(9)] for _ in range(len(s)+1)]
# 初期化
for i in range(len(s)+1):
    dp[i][0] = 1
# Sのi文字目でchokudaiのj文字目が何個完成するか
for i in range(len(s)):
    for j in range(8):
        if s[i] != "chokudai"[j]:
            # 違う文字だったらスキップ
            dp[i+1][j+1]=dp[i][j+1]
        else:
            # 組み合わせが増えるので今の数値と次の数値を足して配る
            dp[i+1][j+1]=(dp[i][j+1]+dp[i][j])%MOD
print(dp[len(s)][-1])
