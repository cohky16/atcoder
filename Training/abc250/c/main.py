n,q = map(int, input().split())
b = list(range(n+1))
pos = list(range(n+1))
for _ in range(q):
    x = int(input())
    t = pos[x]
    tt = t + 1 if t != n else t - 1
    ttt = b[tt]
    b[tt], b[t] = b[t], b[tt]
    pos[x] = tt
    pos[ttt] = t
print(*b[1:])