def to(n):
    return n * (n + 1) // 2

n = int(input())
left = 0
right = n+1
while abs(right-left) > 1:
    mid = abs(right+left)//2
    # n+1の丸太をできる限り分割する
    if to(mid) <= n+1:
        left = mid
    else:
        right = mid
print(n-left+1)