n,m,x = map(int, input().split())
clist = [list(map(int,input().split())) for _ in range(n)]
ans = pow(10, 18)
for i in range(1 << n):
    t = 0
    l = [0]*m
    for j in range(n):
        if i & 1 << j:
            t += clist[j][0]
            for k, c in enumerate(clist[j][1:]):
                l[k] += c
    if min(l) >= x:
        ans = min(t, ans)
print(ans if ans < pow(10, 18) else -1)