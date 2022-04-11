from collections import deque
q = int(input())
d = deque()
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        d.extend([query[1]]*query[2])
    elif query[0] == 2:
        t = 0
        for i in range(query[1]):
            t += d.popleft()
        print(t)