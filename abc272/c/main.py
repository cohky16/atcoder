from itertools import combinations


n = int(input())
aalist = list(map(int, input().split()))
alist = sorted(aalist, reverse=True)[:3]
ans = 0
for a in combinations(alist, 2):
    if sum(a)%2==0:
        ans = max(ans, sum(a))
for a in aalist:
    if alist[0] != a and ans < alist[0]+a and (alist[0]+a)%2==0:
        ans = alist[0]+a
print(-1 if ans == 0 else ans)