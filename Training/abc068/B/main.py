n = int(input())
r = 0
c = 0
for i in range(n + 1):
    t = i
    a = 0
    while t % 2 == 0 and t > 0:
        t /= 2
        a += 1
    if c <= a:
        c = a
        r = i
print(r)
