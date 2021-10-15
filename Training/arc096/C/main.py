a, b, c, x, y = map(int, input().split())
r = 0
if a + b < c * 2: print((a * x) + (b * y))
else:
    while x > 0 or y > 0:
        if x != 0 and y == 0 and a <= c * 2:
            r += a
            x -= 1
        elif y != 0 and x == 0 and b <= c * 2:
            r += b
            y -= 1
        else:
            r += c
            x -= 0.5
            y -= 0.5
    print(r)
