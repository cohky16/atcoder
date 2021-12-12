import bisect
n, q = map(int, input().split())
a = sorted(map(int, input().split()))
l = len(a)
for i in range(q):
    t = int(input())
    b = bisect.bisect_left(a, t)
    print(l - b)