n = int(input())
alist = list(map(int, input().split()))
mi = min(alist)
ma = max(alist)
ans = 1 << 60
for i in range(mi, ma + 1):
    t = 0
    for a in alist:
        t += (a - i)**2
    ans = min(ans, t)
print(ans)
