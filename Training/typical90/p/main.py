from cmath import inf


n = int(input())
a,b,c = map(int, input().split())
l = 10000
ans = pow(10, 18)
for i in range(l):
    if a * i > n: break
    for j in range(l-i):
        if a * i + b * j > n: break
        k = (n - (a*i + b*j))
        if k % c == 0:
            ans = min(ans, i+j+k//c)
print(ans)
