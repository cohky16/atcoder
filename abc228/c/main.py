n, k = map(int, input().split())
l = [sum(map(int, input().split())) for _ in range(n)]
t = sorted(l, reverse=True)[k - 1]
for a in l:
    if t <= a + 300: print("Yes")
    else: print("No")