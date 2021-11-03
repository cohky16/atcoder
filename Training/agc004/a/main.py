a, b, c= map(int, input().split())
r = a*b*c
if r % 2 == 0: print(0)
else:
    print(min(b*c, c*a, a*b))