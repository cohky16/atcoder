n = int(input())
l = list(map(int, input().split()))
r = 0
while (sum(l) > 0):
    r += 1
    f = 0
    for j in range(n):
        if l[j] > 0: 
            l[j] -= 1
            if f == 2: r += 1
            f = 1
        elif f == 1 and l[j] == 0: 
            f = 2
print(r)