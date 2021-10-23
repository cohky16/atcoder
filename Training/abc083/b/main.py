n, a, b = map(int, input().split())
r = 0
for i in range(1, n + 1):
    t = i
    w = 0
    while(t >= 10):
        w += t % 10
        t //= 10
    w += t % 10
    if a <= w <= b: r += i
print(r)