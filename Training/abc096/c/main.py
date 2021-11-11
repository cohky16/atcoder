h, w = map(int, input().split())
l = [input() for i in range(h)]
r = "Yes"
for i in range(h):
    for j in range(w):
        t = 0
        if l[i][j] == "#":
            if i > 0 and l[i - 1][j] == "#": t += 1 # 上
            if j > 0 and l[i][j - 1] == "#": t += 1 # 左
            if j < w - 1 and l[i][j + 1] == "#": t += 1 # 右
            if i < h - 1 and l[i + 1][j] == "#": t += 1 # 下
            if t == 0:
                r = "No"
                break
    if r == "No": break
print(r)