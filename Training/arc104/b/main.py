n,S = input().split()
N = int(n)
ans = 0
for i in range(N):
    t1, t2 = 0, 0
    for j in range(i, N):
        if S[j] == 'A': t1 += 1
        if S[j] == 'T': t1 -= 1
        if S[j] == 'C': t2 += 1
        if S[j] == 'G': t2 -= 1
        if t1 == t2 == 0: ans += 1
print(ans)
