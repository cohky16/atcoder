n,a,x,y = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    if i >= a + 1:
        ans += y
    else:
        ans += x
print(ans)