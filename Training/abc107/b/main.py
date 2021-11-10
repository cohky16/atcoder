h, w = map(int, input().split())
l = [input() for _ in range(h)]
hr = []
for i in range(h):
    if l[i].count(".") != w: hr.append(i)
wr = []
for i in range(w):
    t = 0
    for j in range(h):
        if l[j][i] == ".": t += 1
    if t == h: wr.append(i)
for a in hr:
    ll = l[a]
    t = ""
    for i in range(len(ll)):
        if i not in wr: t += ll[i]
    print(t)