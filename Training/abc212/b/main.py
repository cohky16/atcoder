x = list(map(int, list(input())))
if len(list(set(x))) == 1: print("Weak")
else:
    c = 0
    for i in range(3):
        if x[i] <= 8 and x[i] == x[i + 1] - 1: c += 1
        elif x[i] == 9 and x[i + 1] == 0: c += 1
    print("Strong") if c < 3 else print("Weak")