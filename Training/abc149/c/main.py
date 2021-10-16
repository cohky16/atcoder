x = int(input())
for i in range(x, 1000000):
    flag = True
    for j in range(2, int(x**0.5) + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)
        break