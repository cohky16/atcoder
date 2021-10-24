n = int(input())
t, a = map(int, input().split())
l = list(map(int, input().split()))
r = 1000000
c = 0
for j, i in enumerate(l):
    aa = t - i * 0.006
    if r > abs(a - aa):
        r = abs(a - aa)
        c = j
print(c + 1)

