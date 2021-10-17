import itertools
n = int(input())
l = list(itertools.permutations(range(1, n + 1)))
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
print(abs(l.index(p) - l.index(q)))
