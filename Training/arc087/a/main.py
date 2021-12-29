from collections import Counter
n = int(input())
alist = list(map(int, input().split()))
c = Counter(alist)
ans = 0
for k,v in c.items():
    if v - k >= 0: ans += (v - k)
    else: ans += v
print(ans)