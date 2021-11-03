n, m = map(int, input().split())
a = sorted([list(map(int, input().split())) for i in range(n)])
r = 0
for i in a:
    if i[1] <= m:
        r += i[0] * i[1]
        m -= i[1]
    else:
        r += (i[0] * m)
        break
print(r)