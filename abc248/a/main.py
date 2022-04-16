s = list(map(int, list(input())))
for i in range(10):
    if i not in s:
        print(i)
        exit()
