n,m = map(int, input().split())
alist = [0]+sorted(list(map(int, input().split())))
if alist[-1] != n:
    alist.append(n+1)
salist = [alist[i]-alist[i-1]-1 for i in range(1, len(alist)) if alist[i]-alist[i-1]-1 > 0]
if len(salist) == 0:
    print(0)
    exit()
t = min(salist)
ans = 0
for sa in salist:
    ans += -(-sa//t)
print(ans)
