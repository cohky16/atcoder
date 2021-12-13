n,m,a,b = map(int, input().split())
ans = 0
for i in range(m):
    if n <= a:
        n += b
    c  = int(input())
    if n >= c:
        n -= c
    else:
        ans = i + 1
        break
print("complete") if ans == 0 else print(ans)
