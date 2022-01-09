n = int(input())
xylist = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans,(abs(xylist[i][0] - xylist[j][0])**2 + abs(xylist[i][1] - xylist[j][1])**2)**0.5)
print(ans)