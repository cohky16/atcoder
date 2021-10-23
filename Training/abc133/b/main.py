n, d = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l.append(l[0])
r = 0
for i in range(n):
    for k in range(i + 1, n):
        t = 0
        for j in range(d):
            t += (l[i][j] - l[k][j])**2
        if (t ** 0.5).is_integer(): r += 1
print(r)
