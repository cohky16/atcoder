n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = 0
for i, v in enumerate(b):
    t = v - a[i]
    if t <= 0: r += v
    else:
        r += a[i]
        aa = t - a[i + 1]
        if aa <= 0: r += t
        else: r += a[i + 1]
        a[i + 1] = max(a[i + 1] - t, 0)
print(r)
    