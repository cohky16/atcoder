n = int(input())
k = int(input())
l = list(map(int, input().split()))
r = 0
for x in l:
    r += min(x * 2, (k - x) * 2)
print(r)

