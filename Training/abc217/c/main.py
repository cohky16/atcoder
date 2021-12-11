n = int(input())
p = list(map(int, input().split()))
l = [0]*n
for i in range(n):
    l[p[i] - 1] = i + 1
print(*l)