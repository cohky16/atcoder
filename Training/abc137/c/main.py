from collections import Counter
n = int(input())
slist = Counter(["".join(sorted(input())) for _ in range(n)])
ans = 0
for s in slist.values():
    ans += (s * (s - 1) // 2)
print(ans)
