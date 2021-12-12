n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
INF = 1 << 60
ans =[INF] * n
for i in range(2 * n):
    ans[(i + 1) % n] = min(ans[i % n] + s[i % n], t[(i +1) % n])
for a in ans:
    print(a)