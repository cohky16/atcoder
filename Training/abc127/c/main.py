n, m = map(int, input().split())
aa = 0
bb = 1000000
for i in range(m):
    a, b = map(int, input().split())
    aa = max(a, aa)
    bb = min(b, bb)
r = 0
for i in range(aa, bb + 1):
    if n >= i: r += 1
print(r)
    