from collections import deque
q = int(input())
ans = deque()
for i in range(q):
    t,x = map(int, input().split())
    if t == 1: ans.appendleft(x)
    if t == 2: ans.append(x)
    if t == 3: print(ans[x-1])

