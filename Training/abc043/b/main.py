s = input()

r = []
for c in s:
    if c == "B" and len(r) > 0: r.pop(-1)
    elif c != "B": r.append(c)
print(''.join(r))