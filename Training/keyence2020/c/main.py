n,k,s = map(int, input().split())
ans = [s % 10 ** 9 + 1] *n
for i in range(k):
    ans[i] = s
print(*ans)