import bisect
n = int(input())
alist = list(map(int, input().split()))
aalist = {}
for i,v in enumerate(alist):
    aalist.setdefault(v, []).append(i+1)
q = int(input())
for i in range(q):
    l,r,x = map(int, input().split())
    if x in aalist:
        print(abs(bisect.bisect_left(aalist[x], l)-bisect.bisect_right(aalist[x], r)))
    else:
        print(0)