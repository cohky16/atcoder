n,q = map(int, input().split())
alist = list(map(int, input().split()))
blist = [alist[i+1]-alist[i] for i in range(n-1)]
blist.append(0)
ans = sum(abs(b) for b in blist)
for i in range(q):
    l,r,v= list(map(int, input().split()))
    l,r = l-1,r-1
    b = abs(blist[l-1]) + abs(blist[r])
    if l > 0: blist[l-1] += v 
    if r < n-1: blist[r] -= v
    a = abs(blist[l-1]) + abs(blist[r])
    ans += a - b
    print(ans)