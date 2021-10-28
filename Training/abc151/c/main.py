n,m=map(int,input().split())
l = [0]*n
pe = [0]*n
r=0
for _ in range(m):
    a,p=input().split()
    i = int(a) - 1
    if l[i] == 0:
        if p == "AC":
            if pe[i] > 0:
                r += pe[i]
            l[i] = 1
        elif p == "WA":
            pe[i] += 1
print(sum(l), r)