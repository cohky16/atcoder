n = int(input())
for i in range(1, 555556):
    s = set(str(i))
    if len(s) == 1:
        n -= 1
    if n == 0:
        print(i)
        break