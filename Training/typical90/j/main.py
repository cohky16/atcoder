n = int(input())
ones=[0]
twos=[0]
for i in range(n):
    c,p = map(int, input().split())
    if c == 1: 
        ones.append(ones[len(ones)-1]+p)
        twos.append(twos[len(twos)-1])
    if c == 2: 
        twos.append(twos[len(twos)-1]+p)
        ones.append(ones[len(ones)-1])
q = int(input())
for i in range(q):
    l,r = map(int, input().split())
    print(ones[r]-ones[l-1],twos[r]-twos[l-1])