n,x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i % 2 == 1:  
        ans += (a[i] - 1)
    else:
        ans += a[i]
print("Yes") if ans <= x else print("No")
