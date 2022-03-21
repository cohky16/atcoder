n = int(input())
l=[i for i in range(1, 2*n+2)]
print(l[0], flush=True)
l.remove(l[0])
while (True):
    n = int(input())
    if n == 0: exit()
    l.remove(n)
    print(l[0], flush=True)
    l.remove(l[0])