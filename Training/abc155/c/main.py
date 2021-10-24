import collections
n = int(input())
l = [input() for i in range(n)]
c = collections.Counter(l)
m = c.most_common()[0][1]
r = []
for cc in c.items():
    if cc[1] == m: r.append(cc[0])
print('\n'.join(sorted(r)))
