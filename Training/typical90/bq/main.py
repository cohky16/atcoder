n,k = map(int, input().split())
MOD = 1000000007
# 1つの場合
if n == 1:
    print(k % MOD)
# 3つ以上の場合
else:
    # 1つ目がk種類で2つ目がk-1種類で残り個数を色でべき乗
    print(k*(k-1) * pow(k-2,n-2,MOD)%MOD)