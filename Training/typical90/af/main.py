import itertools
n = int(input())
alist = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
# 両方ダメな場合は両方のリストを作っておく
# x = 1, y = 2 -> 1: [2], 2: [1]
xylist = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    xylist[x].append(y)
    xylist[y].append(x)
ans = pow(10, 18)
for p in itertools.permutations([i for i in range(1, n+1)]):
    t = 0
    f = True
    for i in range(n):
        r = p[i]
        if i > 0:
            l = p[i-1]
            if r in xylist[l]:
                f = False
                break
        t += alist[r-1][i]
    if f:
        ans = min(ans, t)
print(ans if ans != pow(10, 18) else -1)
