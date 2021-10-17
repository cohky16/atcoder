h = int(input())
c = 1
r = 0
while h > 0:
    r += c
    h //= 2
    c *= 2
print(r)