import itertools
n = int(input())
r = 0
t = []
for i in range(n):
    a, b = map(int,input().split())
    t.append([a,b])
l = list(itertools.permutations(range(n)))
for i in l:
    tt = 0
    for j, _ in enumerate(i):
        if j < len(i) - 1:
            tt += ((t[i[j]][0] - t[i[j + 1]][0])**2 + (t[i[j]][1] - t[i[j + 1]][1])**2)**0.5
    r += tt
print(r/len(l))