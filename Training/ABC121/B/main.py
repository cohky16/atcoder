n, m, c = map(int, input().split())
b = list(map(int, input().split()))
r = 0
for i in range(n):
    t = c
    a = list(map(int, input().split()))
    for j in range(m):
        t += a[j] * b[j]
    if t > 0: r += 1
print(r)