n = int(input())
l = map(int, input().split())
r = [0]*8
t = 0
for a in l:
    if 1 <= a <= 399:  r[0] = 1
    elif 400 <= a <= 799:  r[1] = 1
    elif 800 <= a <= 1199:  r[2] = 1
    elif 1200 <= a <= 1599:  r[3] = 1
    elif 1600 <= a <= 1999:  r[4] = 1
    elif 2000 <= a <= 2399:  r[5] = 1
    elif 2400 <= a <= 2799:  r[6] = 1
    elif 2800 <= a <= 3199:  r[7] = 1
    elif 3200 <= a: t += 1
s = sum(r)
print(s if s else 1, s + t)