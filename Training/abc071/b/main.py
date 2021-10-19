s = input()
f = False
for c in "abcdefghijklmnopqrstuvwxyz":
    if c not in s and not f: 
        print(c)
        f = True
if not f: print("None")
