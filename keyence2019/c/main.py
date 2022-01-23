n = int(input())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
if sum(alist) < sum(blist): print(-1)
else:
    for i in range(n):
        