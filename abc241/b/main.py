n,m = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
ans = "Yes"
for b in blist:
    if b not in alist:
        ans = "No"
    else:
        alist.remove(b)
print(ans)