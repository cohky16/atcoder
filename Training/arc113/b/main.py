a,b,c = map(int, input().split())
t = pow(b,c,4)
if t == 0:
    t = 4
print(pow(a,t,10))