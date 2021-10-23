n = int(input())
l = list(map(int, input().split()))
r = 0
i = 0
c = 0
while i < n - 1:
    if l[i] >= l[i + 1]: c += 1
    else: c = 0
    i += 1
    r = max(c, r)
print(r)