w,h,n = map(int, input().split())
ans = [[0]*w for _ in range(h)]
for i in range(n):
    x,y,a = map(int, input().split())
    if a == 1:
        for j in range(h):
            for k in range(x):
                ans[j][k] = 1
    if a == 2:
        for j in range(h):
            for k in range(x, w):
                ans[j][k] = 1
    if a == 3:
        for j in range(h - y, h):
            for k in range(w):
                ans[j][k] = 1
    if a == 4:
        for j in range(h - y):
            for k in range(w):
                ans[j][k] = 1
print(sum([i.count(0) for i in ans]))