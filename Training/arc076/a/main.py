from math import factorial
n,m = map(int, input().split())
mod = 10**9+7
if abs(n - m) >= 2: print(0)
elif abs(n - m) == 1: print((factorial(n) * factorial(m)) % mod)
else: print((2 * factorial(n) * factorial(m)) % mod)