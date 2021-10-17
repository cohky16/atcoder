s = list(input())
r = 1000000
for i in range(len(s) - 2):
    t = int(s[i] + s[i + 1] + s[i + 2])
    r = min(r, abs(753 - t))
print(r)

