n = int(input())
l = list(map(int, input().split()))
r = 1
max = 0
min = 200001
for i in range(0, n):
    if l[i] < max and l[i] < min: 
        r += 1
    if l[i] > max:
        max = l[i]
    if l[i] < min:
        min = l[i]
print(r)
