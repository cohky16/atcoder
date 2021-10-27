n, k = map(int, input().split())
lll = sorted([int(input()) for _ in range(n)])
print(min(lll[i + k - 1] - lll[i] for i in range(n - k + 1)))