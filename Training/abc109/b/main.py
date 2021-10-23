n = int(input())
l = [input()]
f = True
for i in range(1, n):
    t = input()
    if t in l or l[i - 1][-1] != t[0]:
        print("No")
        f = False
        break
    l.append(t)
if f: print("Yes")