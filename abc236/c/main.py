n,m = map(int, input().split())
slist = input().split()
mlist = set(input().split())
for i in range(n):
    if slist[i] in mlist:
        print("Yes")
    else:
        print("No")