n = int(input())
a = list(map(int, input().split()))
all = 3**n
r = 1
for i in range(n):
    if a[i] %2 ==0: r *= 2
print(all - r)
        