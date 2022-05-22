n,k = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
max = max(alist)
ans = "No"
for i, a in enumerate(alist):
    if a == max and i+1 in blist: ans = "Yes"
print(ans)

