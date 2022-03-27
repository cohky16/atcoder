n,p,q = map(int, input().split())
alist = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                for m in range(l+1,n):
                    if (alist[i]*alist[j]%p*alist[k]%p*alist[l]%p*alist[m]%p) == q:
                        ans += 1
print(ans)