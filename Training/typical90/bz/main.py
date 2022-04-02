n,m = map(int, input().split())
dict = {}
for i in range(1, n+1):
    dict[i] = []
for i in range(m):
    a,b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)
ans = 0
for i in range(1,n+1):
    t = 0
    for num in dict[i]:
        if num < i: t += 1
    if t == 1: ans += 1
print(ans)
