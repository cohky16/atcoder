k, a, b = map(int, input().split())
r = 1
if a >= b - 1 or k < a - 1: 
    print(r + k)
else: 
    res = a
    k -= a - 1
    if k % 2 == 1:
        res += 1
        k -= 1
    res += (b - a) * (k // 2)
    print(res)