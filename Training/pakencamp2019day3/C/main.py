n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
r = 0
for i in range(0, m):
    for j in range(i + 1, m):
        t = 0
        for k in range(n):
            t += max(a[k][i], a[k][j])
        r = max(r, t)
print(r)