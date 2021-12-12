import collections
n = int(input())
s = [input() for _ in range(n)]
c = 0
ans = ""
for k,v in collections.Counter(s).items():
    if c < v:
        c = v
        ans = k
print(ans)