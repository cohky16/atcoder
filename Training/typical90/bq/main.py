n,k = map(int, input().split())
MOD = 1000000007
# 1色の場合
if k == 1:
    if n == 1: print(1)
    else: print(0)
# 1つの場合
elif n == 1:
    print(k%MOD)
# 2つの場合
elif n == 2:
    # 色の数のパターン数
    # 1つ目がk種類で2つ目がk-1種類
    print((k*(k-1))%MOD)
# 3つ以上の場合
else:
    # 1つ目がk種類で2つ目がk-1種類で残り個数を色でべき乗
    print(k*(k-1)%MOD * pow(k-2,n-2)%MOD)