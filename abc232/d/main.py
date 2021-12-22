h,w = map(int, input().split())
clist = [input() for _ in range(h)]
dp = [[0]*(w + 1) for _ in range(h + 1)] # グリッドの外も含む
for i in reversed(range(h)):
    for j in reversed(range(w)):
        if clist[i][j] == "#": continue
        dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]) + 1
print(dp[0][0])