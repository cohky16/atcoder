r, g, b, n = map(int, input().split())
ans = 0
for i in range(n // r + 1):
    for j in range((n - i * r) // g + 1):
        if (n - r * i - g * j) % b == 0: ans += 1
print(ans)