s = list(input())
l = [0]*(len(s) + 1)
for i in range(len(s)):
    if s[i] == "<": l[i + 1] = l[i] + 1
for i in reversed(range(1, len(s) + 1)):
    if s[i - 1] == ">": l[i - 1] = max(l[i - 1], l[i] + 1)
print(sum(l))
