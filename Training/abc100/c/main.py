n = int(input())
l = list(map(int, input().split()))
r = 0
for a in l:
    t = a
    while t % 2 == 0:
        t /= 2
        r += 1
print(r)