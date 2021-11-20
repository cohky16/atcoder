n, m = map(int, input().split())
l = list([list(map(int, input().split())) for i in range(m)])
r = 0
for ans in range(1000):
    s = str(ans)
    if len(s) != n: continue
    f = True
    for i in l:
        for j in range(n):
            if j == i[0] - 1 and int(s[j]) != i[1]: f = False
    if f:
        print(ans)
        exit()
print(-1)
