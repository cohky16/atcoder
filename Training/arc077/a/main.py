from collections import deque
n = int(input())
alist = list(map(int, input().split()))

d = deque()
if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            d.append(alist[i])
        else:
            d.appendleft(alist[i])
else:
    for i in range(n):
        if i % 2 == 0:
            d.appendleft(alist[i])
        else:
            d.append(alist[i])
print(*d)