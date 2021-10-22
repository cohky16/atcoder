s = input()
t = s[0]
r = 0
for i in range(1, len(s)):
    if t == s[i] == "1":
        t = "0"
        r += 1
    elif t == s[i] == "0":
        t = "1"
        r += 1
    else:
        t = s[i]
print(r)
