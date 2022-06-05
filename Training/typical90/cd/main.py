l,r = map(int, input().split())
MOD = 1000000007
ans = 0
for i in range(len(str(l))-1,len(str(r))):
    # 最小値 1 -> 10
    L = max(10**i, l)
    # 最大値 1 -> 99
    R = min(10**(i+1)-1, r)
    # 文字数*合計値*個数//2
    t = ((i+1)*(R+L)*(R-L+1)//2)%MOD
    ans = (ans+t)%MOD
print(ans)