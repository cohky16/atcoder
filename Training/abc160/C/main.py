k, n = map(int, input().split())
a = list(map(int, input().split()))
a.append(k+a[0])
r = 0
for i in range(n):
    r = max(r, a[i + 1] - a[i])
print(k - r)