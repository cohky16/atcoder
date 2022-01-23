from itertools import combinations
n = int(input())
alist = [list(map(int, input().split())) for _ in range(n + (n - 1))]
clist = combinations(range(1,n*2+1), 2)
for c in clist:
    print(c)
