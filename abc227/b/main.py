n = int(input())
l = map(int, input().split())
t = []
for a in range(1, 500):
    for b in range(1, 500):
        t.append((4 * a * b) + 3 * a + 3 * b)
r = 0
for aaa in l:
    if aaa not in t: r += 1
print(r)