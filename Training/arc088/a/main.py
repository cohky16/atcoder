x, y = map(int,input().split())
r = 0
while x <= y:
    r += 1
    x *= 2
print(r)