n = int(input())
xlist = list(map(int, input().split()))
xlists = sorted(xlist)
aa = xlists[n // 2]
bb = xlists[n // 2 - 1]
for i in range(n):
    print(aa) if aa > xlist[i] else print(bb)