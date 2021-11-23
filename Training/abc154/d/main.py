n, k = map(int, input().split())
l = list(map(int, input().split()))
a = [0]
for i in range(n):
    a.append(a[i] + ((l[i] + ((l[i] * (l[i] - 1)) / 2)) / l[i]))
r = 0
for i in range(n - k + 1):
    r = max(r, a[i + k] - a[i])
print(r)