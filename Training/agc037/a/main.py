s = input()
b = ""
r = 0
f = False
for i, c in enumerate(s):
    if f:
        f = False
        continue
    if b != c:
        r += 1
        b = c
    else:
        if len(s) - 1 != i:
            r += 1
            b = c + s[i + 1]
        f = True
print(r)