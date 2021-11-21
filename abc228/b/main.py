n, x=map(int, input().split())
l = list(map(int, input().split()))
r = [0]*n
i = x - 1
while (not r[i]):
    r[i] = 1
    i = l[i] - 1
print(sum(r))