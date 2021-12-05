n,w = map(int, input().split())
l = sorted([list(map(int, input().split())) for i in range(n)], reverse=True)
r = 0
for ll in l:
    if w > ll[1]:
        r += (ll[0] * ll[1])
        w -= ll[1]
    else:
        r += (ll[0] * w)
        break
print(r)