d, n = map(int, input().split())
r = 0
for i in range(1, n + 1):
    t = i
    if i == 100: t += 1
    r = 100**d * t
print(r)