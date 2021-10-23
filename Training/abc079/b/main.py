n = int(input())
memo = [2, 1]
r = 0
for i in range(2, n + 1):
    memo.append(memo[i - 2] + memo[i - 1])
print(memo[-1])