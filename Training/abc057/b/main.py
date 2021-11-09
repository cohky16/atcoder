n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
cd = [list(map(int, input().split())) for i in range(m)]
for i in ab:
    t = 10101010101010
    m = 0
    for k, j in enumerate(cd):
        b = abs(i[0]-j[0]) + abs(i[1]-j[1])
        if t > b:
            t = b
            m = k + 1
    print(m)
