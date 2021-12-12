n = int(input())
l = set()
for i in range(n):
    s,t = input().split()
    name = s + " " + t
    if name in l:
        print("Yes")
        exit()
    l.add(name)
print("No")
