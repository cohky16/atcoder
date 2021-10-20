n, k, q = map(int, input().split())
l = [0]*n
for i in range(q):
    t = int(input()) - 1
    l[t] += 1
for r in l:
    if r + k - q > 0: print("Yes")
    else: print("No")
