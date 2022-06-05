n,k = map(int, input().split())
alist = list(map(int, input().split()))
blist = [[] for _ in range(k)]
# iが同じグループ
for i, x in enumerate(alist):
    blist[i%k].append(x)
for i in range(k):
    blist[i].sort()
clist = [0]*n
for i in range(n):
    clist[i] = blist[i%k][i//k]
print("Yes" if clist==sorted(alist) else "No")
