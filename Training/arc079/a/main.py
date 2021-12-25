n,m = map(int, input().split())
ans = 'IMPOSSIBLE'
l1 = set()
lN = set()
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        l1.add(b)
    elif b == n:
        lN.add(a)
if l1 & lN:
    ans = 'POSSIBLE'
print(ans)


