n = int(input())
l = []
for i in range(n - 1):
    a, b = map(int, input().split())
    l.append(a)
    l.append(b)
a = l[0]
b = l[1]
if len(l) // 2 == l.count(a) or len(l) // 2 == l.count(b):
    print("Yes")
else:
    print("No")
