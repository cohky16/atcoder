n, x = map(int, input().split())
l = [abs(x - i) for i in list(map(int, input().split()))]

def gcd(a, b):
    while (b > 0):
        t = a % b
        a = b
        b = t
    return a

if len(l) == 1: print(l[0])
else:
    r = gcd(l[0], l[1])
    for i in range(2, len(l)):
        r = gcd(r, l[i])
    print(r)