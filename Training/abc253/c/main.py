from collections import defaultdict
q = int(input())
s = defaultdict(int)
for i in range(q):
    query = input().split()
    q = query[0]
    if q == '1':
        x = int(query[1])
        s[x] += 1
    elif q == '2':
        x,c = int(query[1]),int(query[2])
        s[x] -= int(c)
        if s[x] <= 0: del s[x]
    elif q == '3':
        l = s.keys()
        print(max(l)-min(l))