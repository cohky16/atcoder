n, m = map(int,input().split())
r = []
for i in range(n):
    t = list(map(int, input().split()))[1:]
    for j in t:
        r.append(j)
p = 0
for i in range(1, m + 1):
    if r.count(i) == n: p += 1
print(p)
