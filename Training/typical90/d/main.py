h,w = map(int, input().split())
alist = [list(map(int, input().split())) for _ in range(h)]
rows = [sum(alist[i]) for i in range(h)]
cols = []
for i in range(w):
    temp = 0
    for j in range(h):
        temp += alist[j][i]
    cols.append(temp)
for i in range(h):
    ans = []
    row = rows[i]
    for j in range(w):
        col = cols[j]
        ans.append(row + col - alist[i][j])
    print(*ans)
