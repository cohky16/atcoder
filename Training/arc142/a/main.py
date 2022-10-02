def f(n):
    t = str(n)[::-1]
    return min(int(t), int(str(t)[::-1]))

n,k = map(int, input().split())
t = k != int(str(k)[::-1])
r = 0
ans=0
i = 0
if f(k) != k: print(0)
else:
    while n >= k and n >= r:
        if i == 0:
            r = int(str(k)[::-1])
        elif i%2==0:
            r*=10
        else:
            k*=10
        i+=1
        ans+=1
    print(ans if t else ans//2)