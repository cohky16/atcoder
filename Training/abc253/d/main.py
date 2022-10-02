from math import gcd


def to(n):
    return n * (n + 1) // 2
def lcm(a, b):
    return a*b // gcd(a,b)
n,a,b = map(int, input().split())
t = lcm(a,b)
print(to(n)-(a*to(n//a))-(b*to(n//b))+(t*to(n//t)))