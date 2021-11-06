s = input()
l = list(set(s))
r = 0
for i in reversed(range(len(s))):
    t = "".join([s[j] for j in range(i)])
    le = len(t)
    if le % 2 == 0 and le > 0:
        aa = t[:-(-le // 2)]
        bb = t[le // 2:]
        if aa == bb: r = max(r, le)
print(r)