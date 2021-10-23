h, w = map(int, input().split())
l = []
t = []
for i in range(h):
    t.append(list(map(int, input().split())))
    for j in range(i + 1, h):
        for k in range(w):
            for m in range(k + 1, w):
                l.append([i, j, k, m])
f = True
for r in l:
    i1, i2, j1, j2 = r[0], r[1], r[2], r[3]
    if t[i1][j1] + t[i2][j2] > t[i2][j1] + t[i1][j2]: f = False
print("Yes") if f else print("No")