n, x = map(int, input().split())
l = list(sorted(map(int, input().split())))
s = sum(l)
if s == x: print(n)
elif s < x: print(n - 1)
else:
    r = 0
    for a in l:
        if x >= a:
            x -= a
            r += 1
        if x == 0: break
    print(r)
