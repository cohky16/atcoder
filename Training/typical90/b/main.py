n = int(input())
if n % 2: exit()
ans = []
for i in range(1 << n):
    t = ""
    c = 0
    for j in range(n):
        # 100 >> 0 -> 100 & 1
        # 100 >> 1 -> 10 & 1
        # 100 >> 2 -> 1 & 1
        if i >> j & 1:
            t += "("
            c += 1
        else:
            t += ")"
            c -= 1
        if c < 0:
            break
    if c == 0:
        ans.append(t)
for s in sorted(ans):
    print(s)
