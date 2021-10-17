n = int(input())
r = 0
t = []
for i in range(n):
    a,b = map(int, input().split())
    t.append([a, b])
    r += a / b
r /= 2
c = 0
for ab in t:
    if r >= ab[0] / ab[1]:
        r -= ab[0] / ab[1]
        c += ab[0]
    else:
        c += (r * ab[1])
        break
print(c)