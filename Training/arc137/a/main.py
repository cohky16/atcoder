from math import gcd


l,r = map(int, input().split())
ans = 0
for i in range(r):
    for j in range(i+1):
        # 最大1500回に1回は条件を満たす
        if gcd(l+j,r-i+j)==1:
            print(r-l-i)
            exit()
print(ans)