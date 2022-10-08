from itertools import combinations


n,m = map(int, input().split())
list = [0]*n
comb = combinations(range(1, n+1), 2)
comblist = [c for c in comb]
for i in range(m):
    k,*xlist = map(int, input().split())
    for c in combinations(xlist, 2):
        if c in comblist:
            comblist.remove(c)
print("Yes" if len(comblist) == 0 else "No")
