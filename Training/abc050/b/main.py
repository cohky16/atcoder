n = int(input())
l = list(map(int, input().split()))
m = int(input())
for i in range(m):
    p, x = map(int, input().split())
    t = 0
    for i, v in enumerate(l):
        if i == p - 1: t += x
        else: t += v
    print(t)