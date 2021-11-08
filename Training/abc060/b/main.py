a, b, c = map(int, input().split())
r = "NO"
for i in range(1, b + 1):
    if a * i % b == c: r = "YES"
print(r)