n = int(input())
b = [input() for _ in range(n)]
m = int(input())
r = [input() for _ in range(m)]
t = list(set(b))
ans = 0
for i in t:
    bb = b.count(i)
    rr = r.count(i)
    ans = max(ans, bb - rr)
print(ans)