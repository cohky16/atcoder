a, b, k = map(int, input().split())

if b - a + 1 >= 2*k:
    for i in range(a, min(a + k, b)):
        print(i)
    for j in range(max(i + 1, (b - k) + 1), b + 1):
        print(j)
else:
    for i in range(a, b + 1):
        print(i)