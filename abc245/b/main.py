n = int(input())
alist = sorted(set(map(int, input().split())))
for i in range(len(alist)):
    if alist[i] != i:
        print(i)
        exit()
print(len(alist))

