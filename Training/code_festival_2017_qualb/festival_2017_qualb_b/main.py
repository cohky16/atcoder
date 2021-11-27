import collections
n = int(input())
a = collections.Counter(map(int, input().split()))
m = int(input())
b = collections.Counter(map(int, input().split()))
r = "YES"
for c in b.items():
    if a[c[0]] < c[1]: r = "NO"
print(r)