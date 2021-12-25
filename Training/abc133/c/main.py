l,r = map(int, input().split())
ans = 1 << 60
for i in range(l, r + 1):
    for j in range(i + 1, r + 1):
        if ans == 0:
            print(ans)
            exit()
        ans = min(ans, (i * j) % 2019)
print(ans)
