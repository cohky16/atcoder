n = int(input())
hlist = list(map(int, input().split()))
ans = 0
for h in hlist:
    if ans < h:
        ans = h
    else:
        break
print(ans)