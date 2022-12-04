n = int(input())
s = list(map(int, input().split()))

a = [0] * n
for i in range(n):
  if i == 0:
    a[i] = s[i]
  else:
    a[i] = s[i] - s[i-1]

print(" ".join(map(str, a)))
