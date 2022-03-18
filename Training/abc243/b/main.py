n = int(input())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
acount=0
bcount=0
for i in range(n):
    if alist[i] == blist[i]: acount += 1
print(acount)
for i in range(n):
    if alist[i] != blist[i] and alist[i] in blist: bcount += 1
print(bcount)
