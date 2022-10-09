H,W,C,Q = map(int, input().split())
query=[list(map(int, input().split())) for i in range(Q)]
ans = [0]*(C+1)
wlist = set()
hlist = set()
# 後ろから塗っていく
for t,n,c in query[::-1]:
    # 塗ってある箇所は塗らない
    if t == 1 and n not in wlist:
        wlist.add(n)
        ans[c] += W - len(hlist)
    elif t == 2 and n not in hlist:
        hlist.add(n)
        ans[c] += H - len(wlist)
print(*ans[1:])
