n = int(input())
alist = list(map(int, input().split()))
sm = 0
t = 0
for i in range(n):
    sm += abs(t - alist[i])
    t = alist[i]
sm += abs(t)

for i in range(n):
    a = alist[i-1] if i else 0
    b = alist[i]
    c = alist[i+1] if i != n - 1 else 0
    ans = sm
    ans -= abs(a-b)
    ans -= abs(b-c)
    ans += abs(a-c)
    print(ans)
