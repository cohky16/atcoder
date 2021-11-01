s = list(map(int, list(input())))
o = ["-", "+"]
rr = ""
for i in range(1 << 3):
    r = s[0]
    t = ""
    t += str(s[0])
    for j in range(3):
        if i&(1 << j):
            r += s[j + 1]
            t += ("+" + str(s[j + 1]))
        else:
            r -= s[j + 1]
            t += ("-" + str(s[j + 1]))
    if r == 7: rr = t + "=7"
print(rr)