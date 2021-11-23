n = int(input())
l = list(map(int, input().split()))
c2 = 0
c4 = 0
c = 0
for i in range(n):
    if l[i] % 4 == 0: c4 += 1
    elif l[i] % 2 == 0: c2 += 1
    else: c += 1
if c4 + 1 == c and n == (c4 + c): print("Yes")
elif c4 < c: print("No")
else: print("Yes")