from math import gcd
def lcm(a, b):
    return a*b // gcd(a,b)
a,b = map(int, input().split())
n = lcm(a,b)
print("Large" if n > 10**18 else n)
