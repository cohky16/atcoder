a, b, c, d = map(int, input().split())

def gcd(c, d): # ユークリッドの互除法
    while (d > 0):
        t = c % d
        c = d
        d = t
    return c

def f(n, c, d):
    g = gcd(c, d) # 最大公約数を求める
    l = c // g * d # c / 最大公約数 * d で最小公倍数を求める
    return n - (n // c) - (n // d) + (n // l) # 全体 - cで割り切れる個数 - dで割り切れる個数 + cとdで割り切れる個数

print(f(b, c, d) - f(a - 1, c, d)) ## [a, b] = [1, b] - [1, a - 1]