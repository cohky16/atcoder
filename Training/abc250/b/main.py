n,a,b = map(int, input().split())
f = False
for i in range(n*a):
    if i % a == 0: f = not f
    ans = ["."]*(n*b)
    ff = f
    for j in range(n*b):
        if j % b == 0: ff = not ff
        if ff: ans[j] = "#"
    print("".join(ans))