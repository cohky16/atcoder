n = int(input())
r = "Yes"
td, xd, yd = 0, 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    d = abs(xd - x) + abs(yd - y)
    tt = t - td
    if tt < d or (tt - d) % 2 == 1:
        r = "No"
        break
    td, xd, yd = t, x, y
print(r)