n = int(input())
l = list(map(int, input().split()))
t = l[0]
f = 0
r = 0
for i in range(1, n):
    if f == 1 and t > l[i]:
        f = 0
        r += 1
        t = l[i]
    elif f == -1 and t < l[i]:
        f = 0
        r += 1
        t = l[i]
    elif t < l[i]:
        f = 1
        t = l[i]
    elif t > l[i]:
        f = -1
        t = l[i]
    else:
        t = l[i]
print(r + 1)