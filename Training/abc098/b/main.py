n = int(input())
s = list(input())
l = list(set(s))
r = 0
for i in range(1, n):
    aa = s[:i]
    bb = s[i:]
    t = 0
    for j in l:
        if j in aa and j in bb: t += 1
    r = max(r, t)
print(r)