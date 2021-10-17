n, a, b = map(int, input().split())
r = n // (a + b) * a
r += min(n % (a + b), a)
print(r)

