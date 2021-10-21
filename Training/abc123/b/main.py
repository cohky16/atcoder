import itertools
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
l = list(itertools.permutations([a, b, c, d, e]))
r = 100000
for i in l:
    t = 0
    for j in range(4):
        if i[j] % 10 > 0:
            t += i[j] + (10 - i[j] % 10)
        else:
            t += i[j]
    r = min(t + i[4], r)
print(r)
