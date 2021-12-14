h,w,n = map(int, input().split())
hl = []
wl = []
for i in range(n):
    a,b = map(int, input().split())
    hl.append(a)
    wl.append(b)
shl = {x: i + 1 for i,x in enumerate(sorted(set(hl)))}
swl = {y: i + 1 for i,y in enumerate(sorted(set(wl)))}
for i in range(n):
    print(shl[hl[i]], swl[wl[i]])

