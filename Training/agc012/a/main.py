n = int(input())
l = sorted(list(map(int, input().split())))
r = sum(l[n::2])
print(r)