n = int(input())
l = list(map(int , input().split()))
r = 0
c = 1
for i in l:
    if i != c: r += 1
    else: c += 1
if r == n:
    print(-1)
else:
    print(r)