from collections import Counter
n = int(input())
ans = Counter(list(input()))
for i in range(n - 1):
    s = Counter(list(input()))
    for k,v in s.items():
        if ans[k]: ans[k] = min(ans[k], v)
    tset = set()
    for c in ans:
        if c not in s.keys(): tset.add(c)
    for t in tset:
        ans.pop(t)
res = ""
for k,v in sorted(ans.items()):
    res += (k * v)
print(res)