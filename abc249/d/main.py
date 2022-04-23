from itertools import product
from collections import Counter
N = int(input())
alist = list(map(int, input().split()))
adict = Counter(alist)
ans = 0
for p in product(range(0,N),repeat=2):
    t = alist[p[0]]/alist[p[1]]
    ans += adict[t]
print(ans)