n = int(input())
l = set()
for i in range(n):
    t = int(input())
    if t not in l: l.add(t)
    else: l.remove(t)
print(len(l))