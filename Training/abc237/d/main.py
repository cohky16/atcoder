from bisect import bisect_left, bisect_right
from collections import deque


n = int(input())
s = input()[::-1]
a = deque()
a.append(n)
for i in range(n):
    if s[i] == 'R':
        a.appendleft(n-i-1)
    else:
        a.append(n-i-1)
print(*a)
