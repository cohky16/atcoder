import collections
n = int(input())
alist = list(map(int, input().split()))
for k,v in collections.Counter(alist).items():
    if v == 3: 
        print(k)
        exit()