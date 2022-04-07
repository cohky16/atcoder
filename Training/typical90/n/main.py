n = int(input())
alist = sorted(list(map(int, input().split())))
blist = sorted(list(map(int, input().split())))
ans = 0
for a,b in zip(alist,blist):
    ans += abs(a-b)
print(ans)