n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
aaa1 = [a1[0]]
for i, a in enumerate(a1):
    if i > 0: aaa1.append(aaa1[i - 1] + a)
r = 0
for i in range(n):
    t = aaa1[i]
    for j in range(i, n):
        t += a2[j]
    r = max(r, t)
print(r)