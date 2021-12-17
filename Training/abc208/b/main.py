import math
p = int(input())
ans = 0
for i in range(10, 0, -1):
    while math.factorial(i) <= p:
        ans += 1
        p -= math.factorial(i)
print(ans)