from collections import Counter
# 約数の組み合わせで高速化
def make_divisors(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.append((i, n//i))
    return res
    
N = int(input())
alist = list(map(int, input().split()))
adict = Counter(alist)
ans = 0
for i in range(N):
    a = alist[i]
    for j,k in make_divisors(a):
        # 組み合わせの数
        if j == k: ans += adict[j]**2
        # 入れ替わりの組み合わせがある
        else: ans += (adict[j] * adict[k] * 2)
print(ans)