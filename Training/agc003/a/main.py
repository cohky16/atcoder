ss = input()
n, w, s, e = 0, 0, 0, 0
for c in ss:
    if c == "N": n += 1
    if c == "W": w += 1
    if c == "S": s += 1
    if c == "E": e += 1
if n == w == s == e or (w == e == 0 and n != 0 and s != 0) or (n == s == 0 and w != 0 and e != 0):
    print("Yes")
else:
    print("No")