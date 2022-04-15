from collections import deque
q = int(input())
d = deque()
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        d.append([query[1], query[2]])
    elif query[0] == 2:
        c = query[1]
        sm = 0
        while c > 0:
            num, cnt = d[0]
            if c >= cnt:
                sm += num * cnt
                d.popleft()
                c -= cnt   
            else:
                sm += num * c
                d[0][1] -= c
                c = 0
        print(sm)