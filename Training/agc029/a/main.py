s = input()
r = 0
c = 0
for i in range(len(s)):
    if s[i] == "W":
        r += (i - c)
        c += 1
print(r)