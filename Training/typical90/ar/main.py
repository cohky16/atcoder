from collections import deque
n,q = map(int, input().split())
alist = deque(map(int, input().split()))
for i in range(q):
    t,x,y = map(int, input().split())
    if t == 1: alist[x-1],alist[y-1] = alist[y-1],alist[x-1]
    elif t == 2: alist.rotate()
    elif t == 3: print(alist[x-1])
