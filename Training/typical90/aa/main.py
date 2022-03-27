n = int(input())
l = set()
for i in range(1,n+1):
    s = input()
    if s not in l:
        print(i)
    l.add(s)