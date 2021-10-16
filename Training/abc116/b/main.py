s = int(input())
r = [s]
for i in range(1000000):
    if r[i] % 2 == 0: t = r[i] // 2
    else: t = 3 * r[i] + 1
    if t in r: break
    else: r.append(t)
print(i + 2)

