n = int(input())
alist = list(map(int, input().split()))
q = int(input())
mlist = list(map(int, input().split()))
ans = set()
for i in range(1 << n):
    t = 0
    for j in range(n):
        if i & (1 << j):
            t += alist[j]
    ans.add(t)
for m in mlist:
    if m in ans: print("yes")
    else: print("no")
