from bisect import bisect, bisect_right
from collections import Counter


n = int(input())
A = list(map(int, input().split()))
alist = sorted(set(A))
sett = Counter()
for i in range(n):
    t = max(len(alist)-bisect_right(alist, A[i]), 0)
    sett[t] += 1
for i in range(n):
    print(sett[i])