a, b, c = map(int, input().split())
r = 0
flag = False
for i in range(40):
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        flag = True
        break
    ta, tb, tc = a, b, c
    a = (ta + tb) / 2
    b = (tb + tc) / 2
    c = (tc + ta) / 2
    r += 1
print(r) if flag else print(-1)