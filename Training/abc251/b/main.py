from itertools import combinations
n,w = map(int, input().split())
alist = list(map(int, input().split()))
ans = set()
for a in alist:
    if a <= w: ans.add(a)
for comb in list(combinations(alist, 2)):
    if sum(comb) <= w: ans.add(sum(comb))
for comb in list(combinations(alist, 3)):
    if sum(comb) <= w: ans.add(sum(comb))
print(len(ans))