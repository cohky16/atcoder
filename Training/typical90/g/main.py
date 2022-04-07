from bisect import bisect
n = int(input())
alist = sorted(list(map(int, input().split())))
q = int(input())
for i in range(q):
    b = int(input())
    idx = bisect(alist, b)
    if idx == 0:
        print(abs(b-alist[0]))
    elif idx >= len(alist):
        print(abs(b-alist[idx-1]))
    else:
        print(min(abs(b-alist[idx-1]),abs(b-alist[idx])))

