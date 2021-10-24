s = input()
r = "AC"
c = 0
for i in range(len(s)):
    if i == 0:
        if s[i] != "A": r = "WA"
    elif 2 <= i <= len(s) - 2:
        if s[i] == "C": c += 1
    else:
        if s[i].isupper(): r = "WA"
if c != 1: r = "WA"
print(r)
