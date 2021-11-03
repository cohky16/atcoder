n = int(input())
a = list(map(int, input().split()))
r = 0
for i in range(n):
    t = a[a[i] - 1] 
    if i == t - 1: r += 1
print(r // 2)