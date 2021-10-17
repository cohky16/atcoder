s = input()
t = s*2
r = []
for i in range(len(s)):
    a = ""
    for j in range(len(s)):
        a += t[i + j]
    r.append(a)
print(min(r))
print(max(r))
