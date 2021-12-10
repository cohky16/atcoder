n = int(input())
a = list(map(int, input().split()))
x = int(input())
total = sum(a)
cnt = x // total
t = 0
ans = 0
for num in a:
    t += num
    ans += 1
    if cnt * total + t > x: break   
print(cnt * n + ans)