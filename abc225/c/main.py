n, m = map(int, input().split())
t = []
r = "Yes"
for i in range(n):
    t.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if j < m - 1 and t[i][j] % 7 == 0: r = "No"
        if j != 0:
            if t[i][j - 1] + 1 != t[i][j]: r = "No"
        if i < n - 1 and t[i][j] + 7 != t[i + 1][j]: r = "No"
print(r)