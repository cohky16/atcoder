s = input()
dp = [0]*(len(s) + 1)
for i in range(len(s)):
    if s[i] in "ACGT":
        dp[i] += 1
        dp[i + 1] += dp[i]
    else:
        dp[i] = 0
print(max(dp))
