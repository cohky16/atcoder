n = int(input())
l = sorted(list(map(int, input().split())))
r = (l[0] + l[1]) / 2
for i in range(2, n):
    r = (r + l[i]) / 2
print(r)
