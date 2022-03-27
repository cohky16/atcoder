from math import gcd
a,b,c = map(int, input().split())
# 切る数字は最大公約数
r = gcd(a, gcd(b,c))
# 各辺ごとに切る回数を求める
print((a//r-1)+(b//r-1)+(c//r-1))
