n = int(input())
l = [int(input()) for i in range(n)]
r = -1
t = l[0]
for i in range(n):
    if t == 2:
        r = i + 1 
        break
    t = int(l[t - 1])
print(r)