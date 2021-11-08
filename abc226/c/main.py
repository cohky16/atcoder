n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
r = 0
t = []
le = len(l)
for i, v in enumerate(reversed(l)):
    if i == 0 or le in t:
        r += v[0]
    t += v[2:]
    le -= 1
print(r)