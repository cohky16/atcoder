n = int(input())
r = 0
for i in range(n + 1):
    if i % 2 != 0:
        c = sum(2 for j in range(2, int(i ** 0.5) + 1) if i % j == 0)
        if c == 6: r += 1
print(r)