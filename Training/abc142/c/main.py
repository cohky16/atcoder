n = int(input())
l = list(map(int, input().split()))
r = [0]*n
for i in range(1, n + 1):
    r[l[i - 1] - 1] = str(i)
print(' '.join(r))