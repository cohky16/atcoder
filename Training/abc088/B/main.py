n = int(input())
l = sorted(list(map(int, input().split())), reverse=True)
a, b = 0, 0
for i in range(n):
    if i % 2 == 0: a += l[i] 
    else: b += l[i]
print(a - b)