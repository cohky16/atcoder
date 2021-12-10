s = list(input())
t = list(input())
r = "No"
if s == t: r = "Yes"
for i in range(len(s) - 1):
    s[i], s[i + 1] = s[i + 1], s[i]
    if s == t: r = "Yes"
    s[i], s[i + 1] = s[i + 1], s[i]
print(r)
