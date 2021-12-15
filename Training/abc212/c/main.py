import bisect
n,m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
ans = 1 << 60
for aa in a:
    i = bisect.bisect(b, aa)
    if 0 <= i - 1 < m:
        b1 = b[i - 1]
        ans = min(ans, abs(b1 - aa))
    if 0 <= i < m:
        b1 = b[i]
        ans = min(ans, abs(b1 - aa))
print(ans)