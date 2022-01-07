n = int(input())
s = input()
wlist = []
elist = []
for i in range(n):
    if s[i] ==  "W":
        wlist.append(1)
        elist.append(0)
    if s[i] ==  "E":
        elist.append(1)
        wlist.append(0)
for i in range(1, n):
    wlist[i] += wlist[i - 1]
    elist[i] += elist[i - 1]
ans = 1 << 60
for i in range(n):
    t = 0
    if i: t += wlist[i - 1]
    t += elist[n - 1] - elist[i]
    ans = min(ans, t)
print(ans)