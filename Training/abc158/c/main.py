a, b = map(int,input().split())
flag = False
for i in range(1, 10001):
    aa = int(i * 0.08)
    bb = int(i * 0.1)
    if aa == a and bb == b and flag == False:
        print(i) 
        flag = True
        break
if not flag: print(-1)
