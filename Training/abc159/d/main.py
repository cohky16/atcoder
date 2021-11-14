import collections
n = int(input())
A = list(map(int, input().split()))
C = collections.Counter(A)
s = 0

for i in list(C.values()):
    s += i * (i - 1) // 2 # 全通りの個数

for i in A:
    print(s - (C[i] - 1)) # 全通りから差分を引く (m - 1) * (m - 2) // 2 = (m * (m - 1) // 2) - ans -> ans = m - 1
        