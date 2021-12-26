from itertools import combinations
n = int(input())
c = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for i in range(n):
    s = input()
    if s[0] in c: c[s[0]] += 1
ans = 0
for cc in combinations(["M", "A", "R", "C", "H"], 3):
    ans += c[cc[0]] * c[cc[1]] * c[cc[2]]
print(ans)