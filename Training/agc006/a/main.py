n = int(input())
s = input()
t = input()
c = 0
for i in range(n):
    if s[i] == t[c]: c += 1
print(n*2 - c)
