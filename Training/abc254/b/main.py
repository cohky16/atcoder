n = int(input())
ans = [[] for _ in range(n)]
for i in range(n):
    ans[i].append(1)
    for j in range(1, i):
        ans[i].append(ans[i-1][j-1]+ans[i-1][j]) 
    if i > 0:
        ans[i].append(1)
    print(*ans[i])
