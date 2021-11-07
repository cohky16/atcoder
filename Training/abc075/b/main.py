h, w = map(int, input().split())
l = [input() for i in range(h)]
for i, r in enumerate(l):
    tt = ""
    for j, c in enumerate(r):
        t = 0
        if c == ".":
            if i != 0 and j != 0 and l[i - 1][j - 1] == "#": t += 1
            if i != 0 and l[i - 1][j] == "#": t += 1
            if i != 0 and j < w - 1 and l[i - 1][j + 1] == "#": t += 1
            if j != 0 and l[i][j - 1] == "#": t += 1
            if j != w - 1 and l[i][j + 1] == "#": t += 1
            if i != h - 1 and j != 0 and l[i + 1][j - 1] == "#": t += 1
            if i != h - 1 and l[i + 1][j] == "#": t += 1
            if i != h - 1 and j < w - 1 and l[i + 1][j + 1] == "#": t += 1
            tt += str(t)
        else:
            tt += c
    print(tt)