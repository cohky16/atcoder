n, k, a = map(int, input().split())
ans = (a + k - 1) % n
print(ans) if ans != 0 else print(n)