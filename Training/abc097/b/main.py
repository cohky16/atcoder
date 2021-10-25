x = int(input())
l = [0]*1001
l[0] = 1
for i in range(2, 32):
    if not l[i]:
        for j in range(2, 32):
            k = i**j
            if x >= k: l[k] = k
print(max(l))