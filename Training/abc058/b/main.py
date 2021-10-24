o = input()
e = input()
l = len(o) + len(e)
co = 0
ce = 0
r = ""
for i in range(l):
    if i % 2 != 0:
        r += e[ce]
        ce += 1
    else:
        r += o[co]
        co += 1
print(r)