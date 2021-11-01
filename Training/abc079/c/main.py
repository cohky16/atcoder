s = list(map(int, list(input())))
o = ["+", "-"]
rr = ""
for i in range(8):
    t = "{:>03s}".format(bin(i)[2:])
    r = s[0]
    for j, c in enumerate(s[1:]):
        if o[int(t[j])] == "+":
            r += c
        elif o[int(t[j])] == "-":
            r -= c
    if r == 7: rr = str(s[0])+o[int(t[0])]+str(s[1])+o[int(t[1])]+str(s[2])+o[int(t[2])]+str(s[3])+"=7"
print(rr)