n, y = map(int, input().split())
r = [-1 , -1, -1]
for i in range(n + 1):
    for j in range(n - i + 1):
        k = n - i - j
        if i * 10000 + j * 5000 + k * 1000 == y:
            r[0], r[1], r[2] = i, j, k
print(*r)