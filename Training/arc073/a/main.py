N, T = map(int, input().split())
L = list(map(int, input().split()))
r = T
for i in range(N - 1):
    r += min(L[i + 1] - L[i], T)
print(r)
