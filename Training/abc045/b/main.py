sa = list(input())
sb = list(input())
sc = list(input())
t = 0
while 1:
    if t == 0: 
        if not sa:
            print("A")
            break
        p = sa.pop(0)
        if p == "a": t = 0
        if p == "b": t = 1
        if p == "c": t = 2
        continue
    elif t == 1: 
        if not sb:
            print("B")
            break
        p = sb.pop(0)
        if p == "a": t = 0
        if p == "b": t = 1
        if p == "c": t = 2
        continue
    elif t == 2: 
        if not sc:
            print("C")
            break
        p = sc.pop(0)
        if p == "a": t = 0
        if p == "b": t = 1
        if p == "c": t = 2
        continue
