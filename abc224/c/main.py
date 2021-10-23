n = int(input())
l = []
l = [list(map(int, input().split())) for i in range(n)]
r = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            dx1 = abs(l[i][0] - l[j][0])
            dx2 = abs(l[i][0] - l[k][0])
            dy1 = abs(l[i][1] - l[j][1])
            dy2 = abs(l[i][1] - l[k][1])
            if dx2 * dy1 != dx1 * dy2: r += 1
print(r)