n,k = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += abs(alist[i]-blist[i])
# 合計の差分より変更回数が小さい場合はNo
if ans > k: print("No")
# 偶奇が一致していた場合はYes
else: print("Yes" if ans % 2 == k % 2 else "No")