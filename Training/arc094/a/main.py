a,b,c=map(int,input().split())
l = [a, b, c]
odd, even = 0, 0
for i in range(3):
    if l[i] % 2 == 0: even += 1
    else: odd += 1
ans = 0
if even == 2:
    ans += 1
    for i in range(3):
        if l[i] % 2 == 0: l[i] += 1
elif odd == 2:
    ans += 1
    for i in range(3):
        if l[i] % 2 != 0: l[i] += 1
r = max(l[0], max(l[1], l[2]))
for i in range(3):
    ans += (r - l[i]) // 2
print(ans)