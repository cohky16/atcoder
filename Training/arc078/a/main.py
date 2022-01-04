n = int(input())
alist = list(map(int, input().split()))
l = [0]
for i in range(n):
    l.append(l[i] + alist[i])
ans = 1 << 60
for i in range(1, n):
    ans = min(ans, abs((l[n] - l[i]) - l[i]))
print(ans)