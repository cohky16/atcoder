n, m = map(int, input().split())
if n == 1 and m == 1:
    print(1)
elif n == 1:
    print(m - 2)
elif m == 1:
    print(n - 2)
else:
    if n == 2 or m == 2: print(0)
    else:
        print((n * m) - (m * 2 + (n - 2) * 2))
