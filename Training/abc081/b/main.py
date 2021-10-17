n = int(input())
aaa = list(map(int, input().split()))
r = 0
while 1:
    bbb = list(filter(lambda x: x % 2 != 0, aaa))
    if len(bbb) > 0: break
    aaa = list(map(lambda x: x / 2, aaa))
    r += 1
print(r)
