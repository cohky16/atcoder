h,w = map(int, input().split())
alist = [list(map(int, input().split())) for _ in range(h)]
blist = [list(map(int, input().split())) for _ in range(h)]
count = 0
for i in range(h-1):
    for j in range(w-1):
        t = blist[i][j]-alist[i][j]
        if t != 0:
            alist[i][j] += t
            alist[i][j+1] += t
            alist[i+1][j] += t
            alist[i+1][j+1] += t
            count += abs(t)
if alist==blist:
    print("Yes")
    print(count)
else:
    print("No")

