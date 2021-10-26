n = list(input())
l = n[1:]
if n.count("9") == len(n) or l.count("9") == len(n) - 1: print(sum(map(int, n)))
else:
    a = int(n[0]) - 1 if len(n) > 1 else int(n[0])
    print((len(n) - 1) * 9 + a)
