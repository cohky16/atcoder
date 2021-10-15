a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
n = int(input())
for i in range(n):
    b = int(input())
    if b in a1: a1[a1.index(b)] = 0
    elif b in a2: a2[a2.index(b)] = 0
    elif b in a3: a3[a3.index(b)] = 0
if a1[0] == a2[0] == a3[0] == 0: print("Yes")
elif a1[0] == a2[1] == a3[2] == 0: print("Yes")
elif a1[0] == a1[1] == a1[2] == 0: print("Yes")
elif a1[1] == a2[1] == a3[1] == 0: print("Yes")
elif a1[2] == a2[2] == a3[2] == 0: print("Yes")
elif a1[2] == a2[1] == a3[0] == 0: print("Yes")
elif a2[0] == a2[1] == a2[2] == 0: print("Yes")
elif a3[0] == a3[1] == a3[2] == 0: print("Yes")
else: print("No")