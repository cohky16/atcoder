n = int(input())
l = list(map(int, input().split()))
r = 0
t = [0]*(max(l) + 2)
for a in l:
    if a > 0:
        t[a - 1] += 1
    t[a] += 1
    t[a + 1] += 1
print(max(t))