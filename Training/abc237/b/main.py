h, w = map(int, input().split())
ans = [[0]*h for _ in range(w)]
for i in range(h):
    alist = list(map(int, input().split()))
    for j in range(w):
        ans[j][i] = alist[j]
for a in ans:
    print(*a)