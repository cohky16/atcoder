from itertools import product
from collections import Counter
n,k = map(int, input().split())
slist = [input() for _ in range(n)]
ans = 0
for p in product((0,1), repeat=n):
    t = ""
    for i in range(n):
        if (p[i]): t += slist[i]
    ans = max(ans,list(Counter(t).values()).count(k))
print(ans)