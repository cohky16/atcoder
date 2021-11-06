h, w = map(int, input().split())
l = [input() for i in range(h)]
for i, r in enumerate(l):
    tt = ""
    for j, c in enumerate(r):
        t = 0
        if c == ".":
            if i != 0 or j != 0:
                if i != 0 and j != 0:
                    if l[i - 1][j - 1] == "#": t += 1 # 左上
                if l[i][j - 1] == "#": t += 1 # 左
                if h - 1 != i:
                    if l[i + 1][j - 1] == "#": t += 1 # 左下
            if i != 0:
                if l[i - 1][j] == "#": t += 1 # 上
            if h - 1 != i:
                if l[i + 1][j] == "#": t += 1 # 下
            if w - 1 != j:
                if i != 0:
                    if  l[i - 1][j + 1] == "#": t += 1 # 右上
                if l[i][j + 1] == "#": t += 1 # 右
                if h - 1 != i:
                    if l[i + 1][j + 1] == "#": t += 1 # 右下
            tt += str(t)
        else:
            tt += c
    print(tt)