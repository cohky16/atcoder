n,k = map(int, input().split())
alist = list(map(int, input().split()))
ans = k // n
mod = k % n
d = {}
for a in alist:
    d[a] = ans 
salist = sorted(alist)
salistl = salist[:mod]
for s in salistl:
    d[s] += 1
for v in d.values():
    print(v)

