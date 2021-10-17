a, b, m = map(int, input().split())
aaa = list(map(int, input().split()))
bbb = list(map(int, input().split()))
r = min(aaa) + min(bbb)
for _ in range(m):
    t = list(map(int, input().split()))
    r = min(aaa[t[0] - 1] + bbb[t[1] - 1] - t[2], r)
print(r)
