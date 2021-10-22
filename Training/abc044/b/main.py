w = input()
l = list(set(list(w)))
flag = True
for c in l:
    if w.count(c) % 2 != 0 and flag == True:
        print("No")
        flag = False
if flag: print("Yes")
