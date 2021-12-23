import bisect
x = int(input())
t = 0
m = 0
while m < x:
    t += 1
    m =( t * (t + 1) )//2
print(t)
