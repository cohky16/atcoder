n = int(input())
res = 0
for i in range(2, int(n**0.5)+1):
    while n % i == 0:
        n /= i
        res += 1
if n != 1: res += 1
ans = 0
tmp = 1
while tmp < res:
    tmp *= 2
    ans += 1
print(ans)
