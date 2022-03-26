n,k = map(int, input().split())
alist =list(map(int, input().split()))
blist= list(map(int, input().split()))
dp=[False]*n
ep=[False]*n
dp[0]=ep[0]=True
for i in range(1,n):
    # aから見る
    if dp[i-1]:
        if (abs(alist[i-1]-alist[i])<=k): dp[i]=True
        if (abs(alist[i-1]-blist[i])<=k): ep[i]=True
    # bから見る
    if ep[i-1]:
        if (abs(blist[i-1]-alist[i])<=k): dp[i]=True
        if (abs(blist[i-1]-blist[i])<=k): ep[i]=True
print("Yes" if dp[-1] or ep[-1] else "No")