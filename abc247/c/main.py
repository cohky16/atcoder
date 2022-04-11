n = int(input())
if n == 1: print(1)
else:
    tlist = [1]
    ans = []
    for i in range(2, n+1):
        ttlist = []
        for t in tlist:
            ttlist.append(t)
        ttlist.append(i)
        for t in tlist:
            ttlist.append(t)
        tlist = []
        for t in ttlist:
            tlist.append(t)
        ans = ttlist
    print(*ans)