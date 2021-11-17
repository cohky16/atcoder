n, k = map(int, input().split())
r = 0
for i in range(1, n + 1):
    c = 0
    t = k
    while(t > i):
        t /= 2
        c += 1
    r += (1 / n) * (1 / 2**c)
print(r)
