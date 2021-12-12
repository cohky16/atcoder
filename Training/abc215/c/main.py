import itertools
s, k = input().split()
k = int(k)
print("".join(sorted(set(itertools.permutations(s)))[k - 1]))