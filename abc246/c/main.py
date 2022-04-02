n,k,x = map(int, input().split())
alist = sorted(list(map(int, input().split())),reverse=True)
i = 0
for i in range(n):
    if k > 0 and alist[i] >= x:
        t = alist[i] // x
        if t <= k:
            alist[i] -= (x*t)
            k -= t
        else:
            alist[i] -= (x*k)
            k = 0
alist = sorted(alist, reverse=True)
i = 0
while k > 0:
    if i >= n: break
    if alist[i] > 0:
        alist[i] = max(alist[i]-x, 0)
        k -= 1
    else:
        i += 1
print(sum(alist))