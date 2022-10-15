from bisect import bisect, bisect_right
from collections import defaultdict


H,W,rs,cs = map(int, input().split())
N = int(input())
one =defaultdict(list)
two = defaultdict(list)
for i in range(N):
    r,c = map(int, input().split())
    one[r].append(c)
    two[c].append(r)
Q = int(input())
for i in range(Q):
    d,l = input().split()
    l = int(l)
    if d == 'L':
        cs -= min(cs-l, min([pow(10, 18)]+[cs-c for c in one[rs]]))
    if d == 'U':
        rs -= min(rs-l, min([pow(10, 18)]+[rs-c for c in two[cs]]))
    if d == 'R':
        cs += min(cs-l, min([pow(10, 18)]+[cs-c for c in one[rs]]))
    if d == 'D':
        rs += min(rs-l, min([pow(10, 18)]+[rs-c for c in two[cs]]))
    print(rs,cs)

