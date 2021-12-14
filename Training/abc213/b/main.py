n = int(input())
l = list(map(int, input().split()))
s = sorted(l)
print(l.index(s[n - 2]) + 1)
