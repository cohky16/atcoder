x, n = list(input()), int(input())
r = []
for i in range(n):
    s = input()
    p = int(''.join(map(str, [x.index(c) + 1 for c in list(s)])))
    t = {
        "priority": '{:<05d}'.format(p),
        "name": s
    }
    r.append(t)
print('\n'.join([v["name"] for v in sorted(r, key=lambda k: k["priority"])]))