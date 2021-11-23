n, l, r = map(int, input().split())
def f(x):
    ans = 0
    for i in range(len(bin(x)[2:])): # 桁が増えるたびに入れ替わるので、2のべき乗分だけ回せばいい
        if 2 ** i ^ n < n: # 条件を満たすかチェック
            ans += min(2 ** (i + 1) - 1, r) - 2 ** i + 1 # 個数をカウント
    return ans
print(f(r) - f(l - 1)) # 1 ~ rと1 ~ lの範囲内で計算する