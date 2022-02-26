n,q = map(int, input().split())
alist = list(map(int, input().split()))
adict = {}
for i in range(n):
    v = alist[i]
    if v not in adict: 
        adict[v] = []
    adict[v].append(i+1)
for i in range(q):
    x,k = map(int, input().split())
    if x in adict and len(adict[x]) >= k: print(adict[x][k-1])
    else: print(-1)
    